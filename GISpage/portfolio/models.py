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
    description = models.TextField()
    category = MultiSelectField(choices=CATEGORIES)
    technologies = models.CharField(max_length=300)
    map_embed = models.TextField()  # HTML iframe or JavaScript snippet for maps
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title
    
# Blog model for my writing and reflections
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(config_name="awesome_ckeditor")
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title