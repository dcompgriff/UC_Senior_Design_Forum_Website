from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
Object that stores information about the year associated with a set of 
senior design projects.
'''
class Year(models.Model):
    class_year = models.DateField()
    

'''
Object that stores information about the degree program for 
a set of senior design projects. 
'''
class DegreeProgram(models.Model):
    degree_program_name = models.TextField()

'''
Model describing a single senior design project. This data is displayed 
as an individual project with data.
'''
class Project(models.Model):
    #Basic information about a project.
    board_image_url = models.TextField()
    abstract = models.TextField()
    member_list = models.TextField()
    advisor = models.TextField()
    future_work = models.TextField()
    topic = models.TextField()
    title = models.TextField()
    
    #Year Reference.
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    #Engineering Class Reference. The CASCADE ensures that if a year is removed, then so are all of the projects for that year.
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)






































