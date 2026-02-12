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
    # PAC FK here
    assignedPac = models.ForeignKey(PACs, on_delete=models.CASCADE)
    def __str__(self):
        return self.name