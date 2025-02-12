from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Project model for my academic and creative work
class Project(models.Model):
    CATEGORIES = [
        ('Urban_Design', 'Urban Design'),
        ('GIS', 'GIS'),
        ('Climate_Resilience', 'Climate Resilience'),
        ('Geography', 'Geography'),
    ]

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    category = MultiSelectField(choices=CATEGORIES)
    technologies = models.CharField(max_length=300)
    mini_map = models.ImageField(upload_to='project_images/', blank=True, null=True)
    image = models.ImageField(upload_to='project_images/')
    detail_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title
    
# Blog model for my writing and reflections
class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    content = RichTextField(config_name='awesome_ckeditor')
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title