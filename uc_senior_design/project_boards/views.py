from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

from .models import Project, DegreeProgram, Year
import json

import boto3
from botocore import exceptions
s3 = boto3.resource('s3')

import uuid
import requests
import base64

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger('django')

'''

'''
def index(request):
    logger.info('LOG MESSAGE FOR RETURNING INDEX!!!')
    return render(request, 'project_boards/index.html')

'''
Return the list of projects for the specified year and degree program.
'''
def projectlist(request, program, year):
    '''
    1) Search for projects in the given year, and given program.
    2) Set the list of objects in a context dictionary.
    3) Render the template with the data.
    '''
    logging.info("degree program: " + str(program))
    logging.info("year: " + str(year))
    
    #Get the year object.
    cyear = Year.objects.filter(year=str(year))
    yearPk = 0
    if len(cyear) > 0:
        yearPk = cyear[0].pk
    else:
        return HttpResponseNotFound()
    
    #Get the degree program.
    cprogram = DegreeProgram.objects.filter(degree_program_name=str(program))
    programPk = 0
    if len(cprogram) > 0:
        programPk = cprogram[0].pk
    else:
        return HttpResponseNotFound()

    #Get the project based on year and degree program.
    projects_list = Project.objects.filter(year=yearPk, degree_program=programPk)
    if len(projects_list) == 0:
        return render(request, 'project_boards/project.html', {'project_list': [], 'empty': True})
    else:
        return render(request, 'project_boards/project.html', {'project_list': projects_list, 'empty': False})

'''
Return the list of all possible years.
'''
def years(request):
    #Get the list of possible years in the database.
    year_object_list = Year.objects.all()
    year_list = []
    for year_object in year_object_list:
        year_list.append(year_object.year)
    
    return HttpResponse(json.dumps({'year_list': year_list}), content_type="application/json")

'''
Convert the json post body to a python dict, create a new Project model, and save it to the DB.
'''
def addProject(request):
    #Convert from json string body to python dict.
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        projectData = json.loads(body_unicode)        
        logging.info("Post Body: " + str(body_unicode))

        bucketName = "uc-senior-design-forum"
        key = "%s-%s" % (str(uuid.uuid4()), projectData["PosterImage"])
        uploadImageFile(projectData['ImageFile'], bucketName, key)

        #Create a new project, set its fields, and save the object to the database.
        newProject = Project(board_image_url=getS3URL(bucketName, key), abstract=projectData["Abstract"], member_list=projectData["Group"], advisor=projectData["Advisor"], future_work=projectData["Futurework"], topic=projectData["Topic"], title=projectData["Title"])
        year = Year.objects.filter(year=str(projectData["Year"]))[0]
        degree_program = DegreeProgram.objects.filter(degree_program_name=projectData["Program"])[0]
        newProject.year = year
        newProject.degree_program = degree_program
        newProject.save()


        response = HttpResponse("success")
        response.status_code = 200
        return response
    else:
        return HttpResponseNotFound()
        
'''
Method returns a template with the csrf token set.
'''
def addProjectForm():
    return render(request, 'project_boards/addproject.html', {})


def uploadImageFile(imageData, bucketName, key):
    imageData = imageData.strip()
    bucket = get_bucket(bucketName)

    # handle errors
    if isinstance(bucket, dict) and 'error' in bucket:
        # if the bucket doesn't exist, make one
        if bucket['error'] == 'Bucket does not exist':
            s3.create_bucket(Bucket=bucketName)
        else:
            return False

    s3.Object(bucketName, key).put(Body=base64.b64decode(imageData[imageData.index(','):]))
    return True


def get_bucket(bucket_name):
    result = s3.Bucket(bucket_name)

    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
    except exceptions.ClientError as e:
        # if it was a 404 error, the bucket doesn't exist
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            result = {'error': 'Bucket does not exist'}
    except exceptions.NoCredentialsError as e:
        result = {'error': 'No credentials found'}
    except:
        result = {'error': sys.exec_info()[0]}

    return result


def getS3URL(bucketName, key):
    return 'https://%s.s3.amazonaws.com/%s' % (bucketName, key)