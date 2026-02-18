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

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

#Form to add students
#Included for the use of a drop-down bar for 'course_choices'
course_choices = [
    ("Computing", "Computing"),
    ("Film Production", "Film Production"),
    ("Game Development", "Game Development"),
]

class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label="Email Address")
    course = forms.ChoiceField(choices=course_choices, label="Course")
    assigned_pac = forms.ModelChoiceField(queryset=PACs.objects.none(),empty_label="Select a PAC", label="Assigned PAC")

    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'email', 'course', 'assigned_pac')

        #Required to assign the form-class to each field for rendering
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "assigned_pac": forms.Select(attrs={"class": "form-select"}),
        }

    #This function makes sure that the list of PACs is calculated at runtime not at import time
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_pac'].queryset = PACs.objects.all()

