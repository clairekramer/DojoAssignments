from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'online/index.html')

def info(request):
    users = User.objects.all()
    context = {
        'all_users' : users
    }
    return render(request, 'online/info.html', context)

def process(request):
    print request.POST
    robot = False
    if request.POST['robot'] == 'on':
        robot = True
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        robot = robot,
    )
    return redirect('/programinfo')
