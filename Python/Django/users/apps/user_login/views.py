from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'user_login/index.html')
