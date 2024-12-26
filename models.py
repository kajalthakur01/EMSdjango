from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()

class Department(models.Model):
    name=models.CharField(max_length=300)
    department=models.CharField(max_length=200)
    salary=models.IntegerField()
    age=models.IntegerField()


class Student(models.Model):
    name=models.CharField(max_length=300)
    course=models.CharField(max_length=200)
    rollno=models.IntegerField()
    age=models.IntegerField()


class ContactEnquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=500)    