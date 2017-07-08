# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print "Displaying Root Route"
    return render(request, 'first_app/index.html')

def testimonials(request):
    print request.method
    print 'Displaying Testimonials'
    return render(request, 'first_app/testimonials.html')

def about(request):
    print 'Displaying About Me'
    return render(request, 'first_app/about.html')

def projects(request):
    print 'Displaying Projects'
    return render(request, 'first_app/projects.html')
# Create your views here.
