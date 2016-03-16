from django.contrib import admin
from models import todo,project, maintask, subtask
# Register your models here.
admin.site.register(todo)
admin.site.register(project)
admin.site.register(maintask)
admin.site.register(subtask)
