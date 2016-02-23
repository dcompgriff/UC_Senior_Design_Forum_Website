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
Return the list of projects for the specified year and degree program.
'''
def projectlist(request, program, year):
#    if (len(str(year)) != 4):
#        response = HttpResponseNotFound('Invalid Year: ' + str(year))
#    else:
#        response = HttpResponse('<p>Hello from the projectlist url.</p><ul><li>'+str(program)+'</li><li>'+str(year)+'</li></ul>')
    
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


def years(request):
    #Get the list of possible years in the database.
    year_object_list = Year.objects.all()
    year_list = []
    for year_object in year_object_list:
        year_list.append(year_object.year)
    
    return HttpResponse(json.dumps({'year_list': year_list}), content_type="application/json")
    #return render(request, 'project_boards/year_list.html', {'year_list': year_list})









