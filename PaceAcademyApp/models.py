from django.db import models

# Create your models here.

class PACs(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Email: {self.email}'

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    course = models.CharField(max_length=100, default='')
    assigned_pac = models.ForeignKey(PACs, on_delete=models.SET_DEFAULT, default = '', related_name = "PACs") #FK linking to pac table

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Email: {self.email}, Course: {self.course}, PAC: {self.assigned_pac}'
