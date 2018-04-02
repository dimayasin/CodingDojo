# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UsersManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name should be more than 1 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name should be more than 1 characters"
        if len(postData['email']) < 5:
            errors["last_name"] = "User last name should be more than 1 characters"
        return errors



class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    objects = UsersManager()




