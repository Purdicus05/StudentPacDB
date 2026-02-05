from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def formSubmission(request):
    return render(request, 'formSubmission.html')

def formSuccess(request):
    return render(request, 'formSuccess.html')