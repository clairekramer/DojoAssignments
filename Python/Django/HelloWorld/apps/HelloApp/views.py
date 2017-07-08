# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print 'Hello World'
    return render(request, 'HelloApp/index.html')
# Create your views here.
