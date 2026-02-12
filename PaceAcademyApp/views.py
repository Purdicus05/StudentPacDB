from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def students(request):
    return render(request, 'students.html')

def pacs(request):
    return render(request, 'pacs.html')