from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def project_detail(request, project_id):
    return render(request, 'portfolio/project_detail.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def about(request):
    return render(request, 'portfolio/about.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

def blog_detail(request, blog_id):
    return render(request, 'portfolio/blog_detail.html')