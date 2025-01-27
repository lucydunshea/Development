from django.contrib import admin
from .models import Project, Blog
from django.utils.html import format_html
class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['title', 'image',]

admin.site.register(Project, ImageAdmin)
admin.site.register(Blog)