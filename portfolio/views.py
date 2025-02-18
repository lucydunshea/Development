from django.shortcuts import render
from .models import Project, Blog
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
   return TemplateResponse(request, 'portfolio/projects.html', {
       'projects': Project.objects.all().order_by('-end_date'),
   })

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
    })

def project_category(request, category):
    projects = Project.objects.filter(category__contains=category).order_by('-end_date')
    return render(request, 'portfolio/projects.html', {
        'projects': projects,
    })

def contact(request):
    return render(request, 'portfolio/contact.html')

def about(request):
    return render(request, 'portfolio/about.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'portfolio/blog.html', {
        'blogs': blogs,
    })

def blog_detail(request, slug):
    blog_post = Blog.objects.get(slug=slug)
    return render(request, 'portfolio/blog_detail.html', {
        'blog_post': blog_post,
    })

def cv(request):
    return render(request, 'portfolio/cv.html')