from django.db import models

# Create your models here.

class PACs(models.Model):
    firstName = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return f'Name: {self.firstName} {self.surname}, Email: {self.email}'

class Students(models.Model):
    firstName = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    course = models.CharField(max_length=100, default='')
    assignedPAC = models.ForeignKey(PACs, on_delete=models.SET_DEFAULT, default = 0, related_name = "PACs") #FK linking to pac table

    def __str__(self):
        return f'Name: {self.firstName} {self.surname}, Email: {self.email}, Course: {self.course}, PAC: {self.assignedPAC}'
