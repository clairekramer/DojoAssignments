from django.shortcuts import render, redirect
from .models import User, Book, Review
from django.contrib.messages import error
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'belt/index.html')

def books(request):
    context = {
        'books': Book.objects.all(),
        'recent': Review.objects.recent(request.POST)
    }
    return render(request, 'belt/books.html', context)

def register(request):
    result = User.objects.validate_reg(request.POST)
    print result
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

def add_book(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'belt/add_book.html', context)

def create(request):
    Review.objects.create_review(request.POST, request.sesion['id'])
    return redirect('/books')

def book_page(request, id):
    context = {
        'book': Book.objects.get(id=id)
    }
    return render(request, 'belt/book_page.html', context)

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
