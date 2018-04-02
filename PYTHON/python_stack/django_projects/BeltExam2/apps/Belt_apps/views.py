from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt
from .models import Users
from .models import Wishlist
import datetime

secret_key = 'TARDIS' 

def index(request):
    users = Users.objects.all()


    request.session['id']=0
    request.session['name']=""
    request.session['item_id'] = 0


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
 
        users = Users.objects.filter(username = request.POST['username'])[0]
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
            username=request.POST['username'], 
            password=hasher1, 
  
            )
        users = Users.objects.filter(username = request.POST['username'])[0]
        context={
            'users': users
        }
        request.session['id'] = users.id
        request.session['name'] = users.name 

        return redirect("/show", context)

def show(request):

    user = Users.objects.filter(id=request.session['id'])[0]
    show_list = Wishlist.objects.filter(added_by = user)
    favelist= Wishlist.objects.filter(Wished_for = user)

    not_fav_list = Wishlist.objects.exclude(added_by = user).exclude(Wished_for= user)


    context={
            'this_wishlist' : show_list,
            'nofaves':not_fav_list ,
            'favelists':favelist
        }
    
 
    return render(request, "wishlist.html", context)

def new_item(request):
    return render(request,"new_list_item.html")

def additem(request):
    errors = Wishlist.objects.ValidateWishList(request.POST)


    if len (errors)>0:
        for error in errors:   
            messages.error(request,error)
        return render(request,"wishlist.html")

    else:
        user = Users.objects.get(id = request.session['id'])
        Wishlist.objects.create( 
            item=request.POST['item'],
            date= datetime.date.today(), 
            added_by= user
        )
        
        wish = Wishlist.objects.filter()
        # request.session['id'] = user.id
        # request.session['name'] = user.name
        context={
            'wishes': wish
        }
        return redirect("/show", context)

def remove(request, id):
    request.session['item_id'] = id
    mylist = Wishlist.objects.get(id=id)
    if mylist.added_by.id == request.session['id']:

        mylist = Wishlist.objects.get(id=request.session['item_id'])
        mylist.delete()

    else:
        messages.error(request,"User doesn't have permission to remove this course")
    return redirect("/show")
def delete(request):
    mylist = Wishlist.objects.get(id=request.session['item_id'])
    mylist.delete()
    return redirect("/show")

def favorites(request, id):
    user = Users.objects.get(name=request.session['name'])

    myfav = Wishlist.objects.get(id=id)

    # get the current user from the database
    # ADD the current user to myfav.Wished_for field
    # save the myfav object
    myfav.Wished_for.add( user)
    myfav.save()

    return redirect("/show")

def notfavorite(request, id):
    # user = Users.objects.filter(request.session['name'])[0]
    Nofav = Wishlist.objects.filter(id=id)[0]
    Nofav.Wished_for = Nofav.added_by
    Nofav.save()

    return redirect("/show")
    

def out(request):
    request.session.clear()
    return redirect ("/log")

def showlist(request,id):

    user_wishes = Users.objects.filter(wished_For=id)
    print user_wishes
    wishes = Wishlist.objects.get(id = id)
   
    names=[]
    for wish in user_wishes:
        names.append(wish.name)
    # request.session['item_name'] = wishes[0].item
    context = {
        'wishes':wishes,
        'names':names
    }
    print names

    return render(request,"this_wish.html", context)