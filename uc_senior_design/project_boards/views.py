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
    if (len(str(year)) != 4):
        response = HttpResponseNotFound('Invalid Year: ' + str(year))
    else:
        response = HttpResponse('<p>Hello from the projectlist url.</p><ul><li>'+str(program)+'</li><li>'+str(year)+'</li></ul>')
    
    return response












