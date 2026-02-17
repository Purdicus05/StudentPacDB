from django.http import HttpResponse
from django.shortcuts import render
from django.template import loaders

from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def students(request):
    return render(request, 'students.html')

def student_from(request):
    return render(request, 'student_form.html')

def pacs(request):
    return render(request, 'pacs.html')

def pac_form(request):
    return render(request, 'pac_form.html')

def form_success(request):
    return render(request, 'form_success.html')

def delete_pac(request, id):
    pac = PACs.objects.get(id=id)
    pac.delete()
    return render(request, 'form_success.html')

def delete_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return render(request, 'form_success.html')

def add_pac(request):
        return render(request, 'add_pac.html')

def add_student(request):
    return render(request, 'add_student.html')

def pac_update(request, id):
    pac = PACs.objects.get(id=id)
    context = {'pac': pac}
    return render(request, 'pac_update.html', context)

def student_update(request, id):
    student = Students.objects.get(id=id)
    context = {'student': student}
    return render(request, 'student_update.html', context)