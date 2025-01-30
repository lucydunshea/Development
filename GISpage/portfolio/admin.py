from django.contrib import admin
from .models import Project, Blog
from django.utils.html import format_html


admin.site.register(Project)
admin.site.register(Blog)