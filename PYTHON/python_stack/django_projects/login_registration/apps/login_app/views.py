# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt
from .models import Users

# Create your views here.

def index(request):
    users = Users.objects.all()

    context ={
        'users': users
    }
    return render(request,"users/index.html", context)

def logins(request):
    errors = Users.objects.validateLoginData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return redirect("/")
    else:
        users = Users.objects.filter(email = request.POST['email'])
        context={
            'users': users
        }
        return render(request,"users/success.html", context)

def Registration(request):
    errors = Users.objects.validateRegistrationData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return redirect("/")
    else:
        hasher1 = bcrypt.hashpw(request.POST['psswrd'].encode(), bcrypt.gensalt())
        Users.objects.create( first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'], password=hasher1)
        users = Users.objects.filter(email = request.POST['email'])
        context={
            'users': users
        }
        return render(request,"users/success.html", context)