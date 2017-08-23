from django.shortcuts import render, redirect
from .models import *

def books(request):
    context = {
        'books': Book.objects.all(),
        'recent': Review.objects.recent(request.POST)
    }
    return render(request, 'belt/books.html', context)

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
