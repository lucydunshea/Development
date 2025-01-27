from django.shortcuts import render
from .models import Project
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
   return TemplateResponse(request, 'portfolio/projects.html', {
       'projects': Project.objects.all(),
   })

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
    })

def contact(request):
    return render(request, 'portfolio/contact.html')

def about(request):
    return render(request, 'portfolio/about.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

def blog_detail(request, blog_id):
    return render(request, 'portfolio/blog_detail.html')

def cv(request):
    return render(request, 'portfolio/cv.html')