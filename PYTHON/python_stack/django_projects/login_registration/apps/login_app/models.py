# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
# Create your models here.

class UsersManager(models.Manager):
    def validateRegistrationData(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("User first name should be more than 2 characters")
        if len(postData['last_name']) < 2:
            errors.append( "User last name should be more than 2 characters")
        if not NAME_REGEX.match(postData["first_name"]):
            errors.append( "First name should contain letters only!")
        if not NAME_REGEX.match(postData["last_name"]):
            errors.append( "Last name should contain letters only!")
        
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

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()