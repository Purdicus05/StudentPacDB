from django import forms

from . import models
from .models import Students, PACs

# Form to add pacs
class AddPacForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        label="First Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter first name"
        })
    )
    last_name = forms.CharField(
        max_length=100,
        label="Last Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter last name"
        })
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "name@example.com"
        })
    )

    class Meta:
        model = PACs
        fields = ('first_name', 'last_name', 'email')
        

#Form to add students
course_choices = [
        ("Computing", "Computing"),
        ("Film Production", "Film Production"),
        ("Game Development", "Game Development"),
    ]

class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        label="First Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter first name"
        })
    )
    last_name = forms.CharField(
        max_length=100,
        label="Last Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter last name"
        })
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "name@example.com"
        })
    )
    course = forms.ChoiceField(
        choices=(course_choices), 
        label="Course",
        widget=forms.Select(attrs={
            "class": "form-select",
            "aria-label": "Select course"
        })
    )
    assigned_pac = forms.ModelChoiceField(
        queryset=PACs.objects.none(),
        empty_label="Select a PAC",
        label="Assigned PAC",
        widget=forms.Select(attrs={
            "class": "form-select",
            "aria-label": "Select PAC"
        })
    )

    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'email', 'course', 'assigned_pac')

    #This function makes sure that the list of PACs is calculated at runtime not at import time
    #This prevents issues with newly added pacs not being shown
    def __init__(self, *args, **kwargs):
        course_choices = kwargs.pop("course_choices", None)
        super().__init__(*args, **kwargs)
        self.fields['assigned_pac'].queryset = PACs.objects.all()
        self.fields['course'].choices = [("", "Select course")] + list(self.fields['course'].choices)


