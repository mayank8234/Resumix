from django.contrib import admin




from .delete import resume_delete
from .login import login
from .signin import signin
from .views import resumes, resume, resume_create, home, edit
from django.urls import path


urlpatterns = [

    path('admin/', admin.site.urls),
    path('resumes/',resumes),
    path('resume/<int:id>',resume),
    path('signin/',signin),
    path('login/',login),
    path('resume_create/',resume_create),
    path('resume_delete/<int:pk>',resume_delete),
    path('home/',home),
    path('edit/<int:pk>',edit),


]