from django.contrib import admin

from .models import DegreeProgram, Project, Year
# Register your models here.

admin.site.register(DegreeProgram)
admin.site.register(Year)
admin.site.register(Project)