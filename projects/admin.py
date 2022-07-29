from django.contrib import admin
from .models import Project, Status, Part, Todo, Td_status, Comment_Part


# Register your models here.

admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Part)
admin.site.register(Todo)
admin.site.register(Td_status)
admin.site.register(Comment_Part)
