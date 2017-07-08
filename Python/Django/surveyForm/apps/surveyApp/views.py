# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveyApp/index.html')

def process(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    request.session['yourName'] = request.POST['yourName']
    request.session['dojoLocation'] = request.POST['dojoLocation']
    request.session['favLanguage'] = request.POST['favLanguage']
    request.session['comment'] = request.POST['comment']
    return redirect ('/results')

def results(request):
    return render(request, 'surveyApp/results.html')
# Create your views here.
