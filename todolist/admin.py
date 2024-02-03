from django.contrib import admin

from todolist.models import Task, Tag


admin.site.register(Task)
admin.site.register(Tag)
