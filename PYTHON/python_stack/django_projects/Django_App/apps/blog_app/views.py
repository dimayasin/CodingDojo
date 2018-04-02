# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    print "this is index"
    return render(request, "index.html")

def new_blog(request):
    print "this is new_blog"
    return render(request,"new_blog.html" )

def create_blog(request):
    print "this is create_blog"
    return render(request,"create_blog.html" )

def show(request):
    print "this is show"
    return render(request,"show.html" )

def edit_number(request):
    print "this is edit"
    return render(request,"edit_number.html" )
    
def delete(request):
    print "this is delete"
    return render(request,"delete.html" )

