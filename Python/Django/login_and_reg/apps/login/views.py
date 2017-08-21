from django.shortcuts import render, redirect
from .models import User
from django.contrib.messages import error
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'login/index.html')

def success(request):
    return render(request, 'login/success.html')

def create(request):
    result = User.objects.validate(request.POST)
    if type(result) == dict:
        for message in result.iteritems():
            error(request, error)
        return redirect('/')
    else:
        context = {
            'user': result
        }
        message = 'Successfully Registered!'
        return render(request, 'login/success.html', context)

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == dict:
        for message in result.iteritems():
            error(request, error)
        return redirect('/')
    context = {
        'user': User.objects.get(id=result.id),
    }
    message = 'Successfully logged in!'
    return render(request, 'login/success.html', context)
