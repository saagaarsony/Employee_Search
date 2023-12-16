from django.db import models

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=100, verbose_name="Employee Name")
    email = models.EmailField(max_length=277, verbose_name="Employee Email")
    mobile = models.IntegerField(verbose_name="Employee Mobile")
    department = models.TextField(max_length=200, verbose_name="Employee Department")
    address = models.TextField(max_length=500, verbose_name="Employee Address")
    dob = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    doj = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    class Foo(models.Model):
        GENDER_CHOICE =( 
        ('M', 'Homme'),
        ('F', 'Femme'),
        )
        gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

class Department(models.Model):
    deptname = models.CharField(max_length=100, verbose_name="Depart name")
    depttype = models.CharField(max_length=100, verbose_name="Department Type")
    deptblock = models.CharField(max_length=100, verbose_name="Department Block")  


    def __str__(self):
        return str(self.id) 
    

