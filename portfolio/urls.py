from django.urls import path, include	
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('projects/category/<str:category>/', views.project_category, name='project_category'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('cv/', views.cv, name='cv'),
    path('ckeditor5/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)