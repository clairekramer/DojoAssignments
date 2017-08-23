from django.shortcuts import render, redirect, reverse
from .models import User
from ..reviews.models import Book
from django.contrib.messages import error

def index(request):
    return render(request, 'belt/index.html')

def register(request):
    result = User.objects.validate_reg(request.POST)
    if type(result) == dict:
        for message in result.iteritems():
            error(request, error)
        return redirect('/')
    else:
        context = {
            'user': result
        }
        return redirect('/books')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == dict:
        for message in result.iteritems():
            error(request, error)
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=result.id)
        }
        return redirect('/books')


def user(request, id):
    user = User.objects.get(id=id)
    group = user.reviews.all().values('book').distinct()
    reviewed_books = []
    for book in group:
        reviewed_books.append(Book.objects.get(id=book['book']))
    context = {
        'user': user,
        'user_reviews': reviewed_books
    }
    return render(request, 'belt/user.html', context)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
