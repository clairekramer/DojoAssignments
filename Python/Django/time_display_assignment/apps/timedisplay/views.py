# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    context = {'current_time' : datetime.now()}
    return render(request, 'timedisplay/index.html', context)
# Create your views here.
