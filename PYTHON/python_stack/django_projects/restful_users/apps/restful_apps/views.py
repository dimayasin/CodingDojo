# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Users



# Create your views here.
def index(request):
    users = Users.objects.all()
    context ={
        'users': users
    }
    return render(request,"users/index.html", context)

def new(request):
    return render(request,"users/new.html")  

    
def show(request):
    context={"users": Users.objects.all()}
    return render(request,"users/show_users.html",context)

def create(request):
    errors = Users.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request,error)
            return redirect("/new")
    else:

        Users.objects.create( first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])

        return redirect("/show")

def edit(request, id):
    user = Users.objects.get(id=id)
    context = {
        "user": user
        }
    return render(request, "users/edit.html", context)


def showuser(request,id):
    user=Users.objects.get(id=id)
    context={"user": user}
    return render(request,"users/user.html",context)

def update(request, id):
    user = Users.objects.filter(id=id)
    edit_user = user[0]
    if request.POST['first_name']:
        edit_user.first_name = request.POST['first_name']
        edit_user.save()
    if request.POST['last_name']:
        edit_user.last_name = request.POST['last_name']
        edit_user.save()
    if request.POST['email']:
        edit_user.email = request.POST['email']
        edit_user.save()
    return redirect("/show")

def delete(request, id):
    Users.objects.filter(id=id).delete()
    return redirect("/show")