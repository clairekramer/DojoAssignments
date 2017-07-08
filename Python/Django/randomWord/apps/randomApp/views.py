# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    return render(request, 'randomApp/index.html')

def generate(request):
    request.session['attempt'] += 1
    request.session['randomWord'] = get_random_string(length=14).upper()
    return redirect('/')

# Create your views here.
