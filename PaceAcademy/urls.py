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
    path('student_form/',views.student_form, name='student_form' ),
    path('add_student/' ,views.add_student, name='add_student' ),

    # Link for description on ' <int:pk> '
    # https://stackoverflow.com/questions/62804254/what-is-the-difference-between-intpk-and-pk
    path("students/<int:pk>/edit/", views.student_update, name="student_update"),

    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),

    path('pacs/', views.pacs, name='pacs'),

    path('pac_form/',views.pac_form, name='pac_form'),

    path("pacs/<int:pk>/edit/", views.pac_update, name="pac_update"),

    path("pacs/<int:pk>/delete/", views.delete_pac, name="pac_delete"),

    path('add_pac/', views.add_pac, name='add_pac'),

    #path('pac_update/', views.pac_update, name='pac_update'),
    #path('pac_delete/', views.delete_pac, name='delete_pac'),
    path('form_success/', views.form_success, name='form_success'),
]
