from django import forms
from .models import Students, PACs

# Form to add pacs
class AddPacForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = PACs
        fields = ('first_name', 'last_name', 'email')

 # Form to add students
class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label="Email Address")
    course = forms.CharField(max_length=100, label="Course")
    assigned_pac = forms.ModelChoiceField(queryset=PACs.objects.none(), label="Assigned PAC")

    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'email', 'course', 'assigned_pac')

    #This function makes sure that the list of PACs is calculated at runtime not at import time
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_pac'].queryset = PACs.objects.all()

