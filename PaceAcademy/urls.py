"""
URL configuration for PaceAcademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PaceAcademyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('student_form/',views.student_from, name='student_from' ),
    path('student_update/', views.student_update, name='student_update'),
    path('pacs/', views.pacs, name='pacs'),
    path('pac_form/',views.pac_form, name='pac_form'),
    path('pac_update/', views.pac_update, name='pac_update'),
    path('form_success/', views.form_success, name='form_success'),
]
