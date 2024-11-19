from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    date_of_birth = models.DateField(null=True,blank=True)    
    

# class Sample(models.Model):
#     name = models.CharField(max_length=10,blank=False,null=False)   #blank = ture(not required field), blank = False(required field)
#     date = models.DateField(auto_now=True)
#     is_active = models.BooleanField() 
#     description = models.TextField(max_length=500,blank=True, null=True)
#     price = models.FloatField()
#     amout = models.DecimalField(max_digits=10,decimal_places=2)
#     appointment_time = models.TimeField(auto_now=True)
#     email = models.EmailField(max_length=20)
#     url = models.URLField()
#     files = models.FileField(upload_to="files/")
#     image = models.ImageField(upload_to="images/")
    
# #onetoone field

# class person(models.Model):
#     f_name = models.CharField(max_length=10)
#     l_name = models.CharField(max_length=10)
    
# class profile(models.Model):
#     user = models.OneToOneField(person,on_delete=models.CASCADE)
#     bio = models.CharField(max_length=50)
#     birthdate = models.DateField(blank=True,null=True)
    
    
# #onetomany(foreignkey)

# class Department(models.Model):
#     name = models.CharField(max_length=15)
    
# class Students(models.Model):
#     name = models.CharField(max_length=10)
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
    
    

# #manytomany

    
# class courses(models.Model):
#     title = models.CharField(max_length=20)
    
# class Employee(models.Model):
#     name = models.CharField(max_length=15)
#     course = models.ManyToManyField(courses,max_length=15)