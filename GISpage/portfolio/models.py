from django.db import models

# Project model for my academic and creative work
class Project(models.Model):
    CATEGORIES = [
        ('Urban Design', 'Urban Design'),
        ('GIS', 'GIS'),
        ('Climate Resilience', 'Climate Resilience'),
        ('Geography', 'Geography'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORIES)
    technologies = models.CharField(max_length=300)
    map_embed = models.TextField()  # HTML iframe or JavaScript snippet for maps
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title