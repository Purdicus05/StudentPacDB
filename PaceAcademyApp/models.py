from django.db import models

# Create your models here.

class PACs(models.Model):
    firstName = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Students(models.Model):
    firstName = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    assignedPAC = models.ForeignKey(PACs, on_delete=models.CASCADE, default = 0) #FK linking to pac table

    def __str__(self):
        return self.name