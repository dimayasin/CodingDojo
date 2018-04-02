# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt
from .models import Users
from .models import Courses
import datetime

secret_key = 'TARDIS' 
context ={}

# Create your views here.
def index(request):
    users = Users.objects.all()
    # errors = []

    request.session['id']=5
    request.session['course_id'] = 0
    request.session['fav'] = []

    context ={
        'users': users
    }
    return render(request, "index.html",context)

def log(request):
    return render(request,"login.html")


def logins(request):
    errors = Users.objects.validateLoginData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return render(request,"login.html")
    else:
 
        users = Users.objects.filter(email = request.POST['email'])[0]
        request.session['id'] = users.id
        request.session['name'] = users.name 

        context={
            'users': users
        }
        return redirect("/show", context)

def new_user(request):
    return render(request,"registration.html")

def Registration(request):
    errors = Users.objects.validateRegistrationData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return render(request,"registration.html")
    else:
        hasher1 = bcrypt.hashpw(request.POST['psswrd'].encode(), bcrypt.gensalt())
        Users.objects.create( 
            name=request.POST['name'],
            email=request.POST['email'], 
            password=hasher1, 
            # DOB= datetime.datetime.strptime(request.POST['DOB'], '%Y-%m-%d')
            )
        users = Users.objects.filter(email = request.POST['email'])[0]
        context={
            'users': users
        }
        request.session['id'] = users.id
        request.session['name'] = users.name 

        return redirect("/show", context)


def addCourse(request):
    # print "addcourses route"
    errors = Courses.objects.ValidateCourses(request.POST)


    if len (errors)>0:
        for error in errors:   
            messages.error(request,error)
        return render(request,"courses.html")

    else:
        user = Users.objects.get(id = request.session['id'])
        Courses.objects.create( 
            name=request.POST['name'],
            description=request.POST['description'], 
            date= datetime.date.today(), 
            user= user
        )
        
        course = Courses.objects.filter()
        # request.session['id'] = user.id
        # request.session['name'] = user.name
        context={
            'courses': course
        }
        return redirect("/show", context)

def show(request):
    show_courses = Courses.objects.filter()
    myfav=[]
    notfav=[]
    for mycourse in show_courses:
        if mycourse.favorite == True:
            myfav += Courses.objects.filter(id=mycourse.id)
        else:
            notfav +=Courses.objects.filter(id=mycourse.id)
    

    context={
            'courses' : notfav,
            "favorites":myfav 
        }
 
    return render(request, "courses.html", context)

def remove(request, id):
    request.session['course_id'] = id
    mycourse = Courses.objects.get(id=id)
    if mycourse.user.id == request.session['id']:
        context ={
            'course':mycourse
        }
        return render(request, "remove.html", context)
    else:
        messages.error(request,"User doesn't have permission to remove this course")
        return redirect("/show")
def delete(request):
    mycourse = Courses.objects.get(id=request.session['course_id'])
    mycourse.delete()
    return redirect("/show")

# def favorites(request, id):
#     mycourses = Courses.objects.filter()
#     myfav = Courses.objects.get(id=id)
#     context = {
#         "course":mycourses,
#         "favorite":myfav
#     }

#     return render(request,"courses.html", context)


def favorites(request, id):

    myfav = Courses.objects.get(id=id)
    myfav.favorite = True
    myfav.save()

    return redirect("/show", context)

def out(request):
    request.session.clear()
    return redirect ("/log")
    