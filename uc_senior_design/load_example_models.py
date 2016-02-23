# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:47:20 2016

@author: dcompgriff
"""

from project_boards.models import Project, DegreeProgram, Year
import project_boards.models as models


def saveModels():
    #Save the years
    models.year1.save()
    models.year2.save()

    #Save degree programs.
    models.degreeProgram1.save()
    models.degreeProgram2.save()
    models.degreeProgram3.save()
    models.degreeProgram4.save()
    models.degreeProgram5.save()
    models.degreeProgram6.save()
    
    #Load projects and save.
    models.testProject1.year = models.year1
    models.testProject2.year = models.year1
    models.testProject3.year = models.year2
    models.testProject1.degree_program = models.degreeProgram1
    models.testProject2.degree_program = models.degreeProgram1
    models.testProject3.degree_program = models.degreeProgram2
    
    models.testProject1.save()
    models.testProject2.save()
    models.testProject3.save()





