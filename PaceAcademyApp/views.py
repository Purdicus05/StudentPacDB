from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def students(request):
    return render(request, 'students.html')

def student_from(request):
    return render(request, 'student_form.html')

def student_update(request):
    return render(request, 'student_update.html')

def pacs(request):
    return render(request, 'pacs.html')

def pac_form(request):
    return render(request, 'pac_form.html')

def pac_update(request):
    return render(request, 'pac_update.html')

def form_success(request):
    return render(request, 'form_success.html')



