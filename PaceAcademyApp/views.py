from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loaders
from .forms import AddStudentForm, AddPacForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def students(request):
    student_list = Students.objects.select_related("assigned_pac").all().order_by("last_name", "first_name")
    return render(request, "students.html", {"students": student_list})

def student_form(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("form_success")
    else:
        form = AddStudentForm()
    return render(request, "student_form.html", {"form": form})

def pacs(request):
    pac_list = PACs.objects.all().order_by("id")
    return render(request, "pacs.html", {"pacs": pac_list})

def pac_form(request):
    if request.method == "POST":
        form = AddPacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("form_success")
    else:
        form =  AddPacForm()
    return render(request, "pac_form.html", {"form": form})

def form_success(request):
    return render(request, 'form_success.html')

def delete_pac(request, pk):
    # Deleting record using 'pk' Values
    pac = get_object_or_404(PACs, pk=pk)
    if request.method == "POST":
        pac.delete()
        return redirect("pacs")
    return render(request, "pac_delete.html", {"pac": pac})

def student_delete(request, pk):
    #Deleting record using 'pk' Values
    student = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("students")
    return render(request, "student_delete.html", {"student": student})

def add_pac(request):
        return render(request, 'add_pac.html')

def add_student(request):
    return render(request, 'add_student.html')



def pac_update(request, pk):
    pac = get_object_or_404(PACs, pk=pk)
    if request.method == "POST":
        form = AddPacForm(request.POST, instance=pac)
        if form.is_valid():
            form.save()
            return redirect("pacs")
    else:
        # Pulling the pre-filled form
        form = AddPacForm(instance=pac)
    return render(request, "pac_form.html", {"form": form, "pac": pac, "is_edit": True})

def student_update(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        #Pulling the pre-filled form
        form = AddStudentForm(instance=student)
    return render(request, "student_form.html", {"form": form, "student": student, "is_edit": True})