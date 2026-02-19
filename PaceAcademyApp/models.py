from django.db import models


# Defines database tables
class PACs(models.Model):
    id = models.AutoField(primary_key=True) #Automatically assigned primary key
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')

    #Meta class improves readability for user
    class Meta :
        verbose_name = "PAC"
        verbose_name_plural = 'PACs'

    #Returned when add completed
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    course = models.CharField(max_length=100, default='')
    assigned_pac = models.ForeignKey(PACs, on_delete=models.SET_NULL, null = True, blank = True, related_name = "PACs") #FK linking to pac table

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, PAC ID = {self.assigned_pac.id}"


