from django.contrib import admin

from app.models import Task, Tag


admin.site.register(Task)
admin.site.register(Tag)
