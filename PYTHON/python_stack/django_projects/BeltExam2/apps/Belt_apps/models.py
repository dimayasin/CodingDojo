from __future__ import unicode_literals

from django.db import models
import datetime
import re, bcrypt
import django.utils



NAME_REGEX = re.compile(r'^[a-zA-Z+ ]+$')
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

# Create your models here.
class UsersManager(models.Manager):
    def validateRegistrationData(self, postData):
        errors = []

        if len(postData['name']) <= 3:
            errors.append("Name should be more than 3 characters")
        if not NAME_REGEX.match(postData["name"]):
            errors.append( "Name should contain letters only!")       
        if len(postData['username']) <= 3:
            errors.append("Username should be more than 3 characters")
        if not USER_REGEX.match(postData["name"]):
            errors.append( "User name should contain letters only!")       

        if len(postData['psswrd']) < 8:
            errors.append( "User password should be more than 8 characters")
        if not postData['psswrd'] == postData['cpsswrd']:
            errors.append( "User passwords do not match.")
            
        test = Users.objects.filter(username = postData['username'])
        if test :
            errors.append( "Username already exists.")


        return errors

    def validateLoginData(self, postData):
        errors = []
        if not postData['username']:
            errors.append("Username is needed for login.")
        if not postData['psswrd']:
            errors.append("Password is needed for login.")
        if Users.objects.filter(username = postData['username']):
            obj= Users.objects.get(username = postData['username'])
            temp=obj.password
            if not bcrypt.checkpw(postData['psswrd'].encode(),temp.encode()):
                errors.append("Invalid Password")
        else:
            errors.append( "There is no registered Username")

        if len(postData['psswrd']) < 8:
            errors.append( "User password should be more than 8 characters")

        return errors


class WishlistManager(models.Manager):
    def ValidateWishList(self, postData):
        errors=[]
        if not postData['item']:
            errors.append("Item field should have a value.") 
        if len(postData['item']) < 3:
             errors.append("Item name should be more than 3 characters")
        

        return errors


   
class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()





class Wishlist(models.Model):
    item = models.CharField(max_length=255)
    favorites=models.BooleanField(default=False)
    Wished_for = models.ManyToManyField(Users,related_name="wished_For")
    date = models.DateField(default= django.utils.timezone.now())#datetime.date.today())
    added_by = models.ForeignKey(Users, related_name="added_by")
    objects = WishlistManager()

    