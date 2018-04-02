# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import re, bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z+ ]+$')
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

# Create your models here.
class UsersManager(models.Manager):
    def validateRegistrationData(self, postData):
        errors = []

        if len(postData['name']) < 2:
            errors.append("User name should be more than 2 characters")
        if not NAME_REGEX.match(postData["name"]):
            errors.append( "User name should contain letters only!")       
        if  not EMAIL_REGEX.match(postData['email']) or not re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",postData['email']):
            errors.append( "Invalid Email Address.")
        if len(postData['psswrd']) < 8:
            errors.append( "User password should be more than 8 characters")
        if not postData['psswrd'] == postData['cpsswrd']:
            errors.append( "User passwords do not match.")
            
        test = Users.objects.filter(email = postData['email'])
        if test :
            errors.append( "Email already exists.")


        return errors

    def validateLoginData(self, postData):
        errors = []
        if not postData['email']:
            errors.append("Email is needed for login.")
        if not postData['psswrd']:
            errors.append("Password is needed for login.")
        if Users.objects.filter(email = postData['email']):
            obj= Users.objects.get(email = postData['email'])
            temp=obj.password
            if not bcrypt.checkpw(postData['psswrd'].encode(),temp.encode()):
                errors.append("Invalid Password")
        else:
            errors.append( "There is no registered email address")

        if not re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",postData['email']):
            errors.append("User email has the wrong format.")
        if len(postData['psswrd']) < 8:
            errors.append( "User password should be more than 8 characters")

        return errors

class CoursesManager(models.Manager):
    def ValidateCourses(self, postData):
        errors=[]
        if not postData['name'] or not postData['description']:
            errors.append("All field should have values.") 
        if len(postData['name']) < 5:
             errors.append("Course name should be more than 5 characters")
        if len(postData['description']) < 15:
             errors.append("Course Description should be more than 15 characters")


        return errors

   
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()


class Courses(models.Model):
    name = models.CharField(max_length=255)
    favorite=models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    date = models.DateField(default= datetime.date.today())
    user = models.ForeignKey(Users, related_name="user_course")
    objects = CoursesManager()

