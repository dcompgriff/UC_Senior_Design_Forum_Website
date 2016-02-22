from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

from .models import Project, DegreeProgram

# Create your views here.

'''
Return the list of projects for the specified year and degree program.
'''
def projectlist(request, program, year):
    response = None
#    if (len(str(year)) != 4):
#        response = HttpResponseNotFound('Invalid Year: ' + str(year))
#    else:
#        response = HttpResponse('<p>Hello from the projectlist url.</p><ul><li>'+str(program)+'</li><li>'+str(year)+'</li></ul>')
    
    '''
    1) Search for projects in the given year, and given program.
    2) Set the list of objects in a context dictionary.
    3) Render the template with the data.
    '''
    projects_list = Project.objects.filter(year=str(year), degree_program=program)
    if len(projects_list) == 0:
        return HttpResponseNotFound("<h1>The projects for the year and/or program your are requesting can't be found.</h1>")
    else:
        return render(request, 'project_boards/project.html', {'project_list': projects_list})












