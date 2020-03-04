from django.contrib import admin
from .models import Project, ProjectApplication, ProjectAssignment, Notification
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectApplication)
admin.site.register(ProjectAssignment)
admin.site.register(Notification)
