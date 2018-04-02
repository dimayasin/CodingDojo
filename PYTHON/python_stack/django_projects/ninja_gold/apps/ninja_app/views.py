# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import datetime


# Create your views here.


def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['msg'] = ""

    return render(request, 'ninja/index.html')


def process_money(request):
    Value = request.POST['building']
    now = datetime.datetime.now()
    # print type(Value)
    money =0


    # game_time=datetime.datetime.fromtimestamp(1518377161).isoformat()
    if  Value == "farm" :
        # request.session['gold'] += random.randrange(10,21)
        money = random.randint(10,20)
        request.session['gold'] += money
        request.session['msg'] +="\n Earned "+str(money)+". Balance is: "+str(request.session['gold'])+" golds from the farm!"+str(now)
    elif Value == "cave" :
        # request.session['gold'] += random.randrange(5,11)
        money = random.randint(5,10)
        request.session['gold'] += money
        request.session['msg'] +="\n Earned "+str(money)+". Balance is: "+str(request.session['gold'])+" golds from the farm!"+str(now)
    elif Value == "house" :
        # request.session['gold'] += random.randrange(2,6)
        money = random.randint(2,5)
        request.session['gold'] += money
        request.session['msg'] +="\n Earned "+str(money)+". Balance is: "+str(request.session['gold'])+" golds from the farm!"+str(now)
    elif Value == "casino" :
        # request.session['gold'] += random.randrange(-50,51)
        money = random.randint(-50,50)
        request.session['gold'] += money
        if money < 0:
          request.session['msg'] +="\n Lost "+str(money)+". Balance is: "+str(request.session['gold'])+" golds from the farm!"+str(now) 
        else:
          request.session['msg'] +="\n Earned "+str(money)+". Balance is: "+str(request.session['gold'])+" golds from the farm!"+str(now) 
  
    # context = {
    #     'gold': request.session['gold'],
    #     'msg': request.session['msg']
    # }

    return redirect("/")
def reset(request):
    
    request.session['gold'] = 0
    request.session['msg'] = ""
    return redirect("/")
