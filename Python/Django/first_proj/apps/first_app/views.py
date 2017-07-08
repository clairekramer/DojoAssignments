# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'first_app/index.html')
def show(request):
    print request.method
    return render(request, 'first_app/showusers.html')
def create(request):
    print request.method
    if request.method == 'POST':
        print (request.POST)
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')
