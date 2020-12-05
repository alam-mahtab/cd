from django.db import models
from django import forms
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
#from django.core.validators import RegexValidator

#alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# Create your models here.
class Schedule(models.Model):
    # id : int      as we are using db we do not need id
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Schedule2(models.Model):
    # id : int      as we are using db we do not need id
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Schedule3(models.Model):
    # id : int      as we are using db we do not need id
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Highlight(models.Model):

    #id : int
    image = models.ImageField(upload_to ='pics')
    work = models.CharField(max_length=100)
    worktype = models.CharField(max_length=200)
    description = models.TextField()

class User_Data(models.Model):
    #objects =  UserManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    CD_Id = models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Inquiry(models.Model):
    first_name = models.CharField(max_length=50)
    interview = models.BooleanField(default=False)
    work_or_commision = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    email = models.EmailField()
    Details = models.TextField()

