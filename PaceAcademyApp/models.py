from django.db import models

# Create your models here.

class PACs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    assignedPAC = models.ForeignKey(PACs, on_delete=models.CASCADE) #FK linking to pac table

    def __str__(self):
        return self.name