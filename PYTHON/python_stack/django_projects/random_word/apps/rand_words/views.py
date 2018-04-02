# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
  context = {
  "string": get_random_string(length=14)
    }
  return render(request,'rwords/index.html', context)