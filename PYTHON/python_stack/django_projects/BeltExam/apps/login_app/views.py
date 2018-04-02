# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt
from .models import Users
from .models import Posts
import datetime

secret_key = 'TARDIS' 


def index(request):
    users = Users.objects.all()
    request.session['name'] = ""
    request.session['id']=0
    request.session['post_id'] = 0

    context ={
        'users': users
    }
    return render(request,"index.html", context)

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
            DOB= datetime.datetime.strptime(request.POST['DOB'], '%Y-%m-%d'))
        users = Users.objects.filter(email = request.POST['email'])[0]
        context={
            'users': users
        }
        request.session['id'] = users.id
        request.session['name'] = users.name 

        return redirect("/show", context)

def new_user(request):
    return render(request,"registration.html")

def Newappointments(request):

    errors = Posts.objects.ValidatePosts(request.POST)
    # print str(request.POST['date'])
    # print str (datetime.date.today())

    if len (errors)>0:
        for error in errors:   
            messages.error(request,error)
        return render(request,"add_appt.html")
    else:

        Posts.objects.create( 
            task=request.POST['task'],
            time=request.POST['time'], 
            status='Pending', 
            date= datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d'), 
            user_id= request.session['id']
        )
        posting = Posts.objects.filter(user_id = request.session['id'])
        # request.session['id'] = user.id
        # request.session['name'] = user.name
        context={
            'posts': posting
        }
        return redirect("/show", context)

def update(request):
    # request.session['post_id'] = id
    posts = Posts.objects.filter(id=request.session['post_id'])
    edit_post = posts[0]
    if not request.POST['task'] == edit_post.task:
        edit_post.task = request.POST['task']
        edit_post.save()
    if not request.POST['status'] == "Select a Status":
        edit_post.status = request.POST['status']
        edit_post.save()
    if not datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d') == datetime.datetime.strptime(edit_post.date, '%Y-%m-%d'):
        edit_post.date = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d')
        edit_post.save()
    if not request.POST['time'] == edit_post.time:
        edit_post.time = request.POST['time']
        edit_post.save()

    return redirect("/show")

def delete(request):
    Users.objects.filter(id=request.session['id']).delete()
    return redirect("/show")

def out(request):
    request.session.clear()
    return redirect ("/log")
def add(request):
    users = Users.objects.filter(id = request.session['id'])
    # users = myusers[0]
    context={
        'users': users
        }
    
    return render(request,"add_appt.html", context)

def show(request):
    ShowToday = []
    ShowFuture = []
    show_posts = Posts.objects.filter(user_id = request.session['id'])
    for val in show_posts:
        # if datetime.datetime.strptime(val.date, '%Y-%M-%d') ==  datetime.datetime.today() :
        if val.date ==  datetime.date.today() :
            ShowToday.append(val)
        # elif datetime.datetime.strptime(val.date, '%Y-%M-%d') >  datetime.datetime.today() :
        elif val.date >  datetime.date.today() :
            ShowFuture.append(val)


    context={
        "today_posts":ShowToday ,
        "future_posts":ShowFuture 
        }
    
    return render(request, "appointments.html", context)

def edit(request,id):
    posting = Posts.objects.filter(id = id)[0]
    context={
        'posts': posting
    }

    return render(request,"appt_form.html",context)
