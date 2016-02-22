from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
    

'''
Object that stores information about the degree program for 
a set of senior design projects. 
'''
@python_2_unicode_compatible 
class DegreeProgram(models.Model):
    
    def __str__(self):
        return unicode(self.degree_program_name)
    
    degree_program_name = models.TextField(unique=True)

'''
Model describing a single senior design project. This data is displayed 
as an individual project with data.
'''
@python_2_unicode_compatible 
class Project(models.Model):
    
    def __str__(self):
        return unicode(self.log_form())
        
    def log_form(self):
        niceOutputString = ''
        niceOutputString += self.board_image_url + '\n'
        niceOutputString += self.abstract + '\n'
        niceOutputString += self.member_list + '\n'
        niceOutputString += self.advisor + '\n'
        niceOutputString += self.future_work + '\n'
        niceOutputString += self.topic + '\n'
        niceOutputString += self.title + '\n'    
    
    #Basic information about a project.
    board_image_url = models.TextField()
    abstract = models.TextField()
    member_list = models.TextField()
    advisor = models.TextField()
    future_work = models.TextField()
    topic = models.TextField()
    title = models.TextField()
    year = models.TextField()

    #Engineering Class Reference. The CASCADE ensures that if a year is removed, then so are all of the projects for that year.
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE, to_field='degree_program_name')



'''
Project(board_image_url='/myimage.jpg', abstract='This is the abstract', 
member_list='FName, SName, TName', advisor='Dr man', future_work='Awesome future projects',
topic='mtopic', title='mtitle', year='2016')
'''


































