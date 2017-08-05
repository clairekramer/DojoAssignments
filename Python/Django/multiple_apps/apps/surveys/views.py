from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = 'placeholder to display all the surveys created'
    HttpResponse(response)

def new(request):
    response = 'placeholder for users to add a new survey'
    HttpResponse(response)
