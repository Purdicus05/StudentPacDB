from django.shortcuts import render

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
    template = loader.get_template('pac_form.html')
    return HttpResponse(template.render({}, request))

def add_student(request):
    template = loader.get_template('student_form.html')
    return HttpResponse(template.render({}, request))

def update_pac(request, id):
    pac = PACs.objects.get(id=id)
    template = loaders.get_template('pac_update.html')
    context = {'pac': pac}
    return HttpResponse(template.render(context, request))

def update_student(request, id):
    student = Students.objects.get(id=id)
    template = loaders.get_template('student_update.html')
    context = {'student': student}
    return HttpResponse(template.render(context, request))