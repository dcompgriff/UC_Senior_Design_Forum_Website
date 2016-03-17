from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

from .models import Project, DegreeProgram, Year
import json

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

'''

'''
def index(request):
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
    projects_list = Project.objects.filter(year=str(year), degree_program=program.strip())
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
        #Create a new project, set its fields, and save the object to the database.
        newProject = Project(board_image_url=projectData["PosterImage"], abstract=projectData["Abstract"], member_list=projectData["Group"], advisor=projectData["Advisor"], future_work=projectData["Futurework"], topic=projectData["Topic"], title=projectData["Title"])
        year = Year.objects.filter(year=str(projectData["Year"]))[0]
        degree_program = DegreeProgram.objects.filter(degree_program_name=projectData["Program"])[0]
        newProject.year = year
        newProject.degree_program = degree_program
        newProject.save()
        
        uploadImageFile(projectData['ImageFile'])

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

def uploadImageFile(imageData):
    pass