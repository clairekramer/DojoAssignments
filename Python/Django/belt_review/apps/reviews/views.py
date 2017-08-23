from django.shortcuts import render, redirect
from .models import *

def books(request):
    context = {
        'more': Review.objects.all(),
        'recent': Review.objects.recent()[0]
    }
    return render(request, 'reviews/books.html', context)

def add_book(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'reviews/add_book.html', context)

def create(request):
    print request.POST
    Review.objects.create_review(request.POST, request.session['user_id'])
    return redirect('/books')

def book_page(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'reviews/book_page.html', context)

def create_additional(request, book_id):
    book = Book.objects.get(id=book_id)
    new_review = {
        'title': book.title,
        'author': book.author.id,
        'rating': request.POST['rating'],
        'comment': request.POST['review'],
        'new_author': ''
    }
    Review.objects.create_review(new_review, request.session['user_id'])
    return redirect(book_id)
