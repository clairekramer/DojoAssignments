from django.shortcuts import render, redirect
from .models import User
from django.contrib.messages import error
from django.core.urlresolvers import reverse
import bcrypt

def index(request):
    return render(request, 'login/index.html')

def success(request):
    return render(request, 'login/success.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for tag, message in errors.iteritems():
            error(request, message, extra_tags=tag)
        return redirect('/')
    hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed
    )
    context = {
        'user': User.objects.last()
    }
    message = 'Successfully Registered!'
    return render(request, 'login/success.html', context)

def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for tag, message in errors.iteritems():
            error(request, message, extra_tags=tag)
        return redirect('/')
    context = {
        'user': User.objects.get(id=check.id),
    }
    message = 'Successfully logged in!'
    return render(request, 'login/success.html', context)
