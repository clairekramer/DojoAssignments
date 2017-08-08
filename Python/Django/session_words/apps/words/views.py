from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'words/index.html')

def add(request):
    request.session['date'] = datetime.now().strftime('%H:%M %p, %B %d, %Y')
    request.session['new_word'] = request.POST['new_word']
    request.session['color'] = request.POST['color']
    if 'size' in request.POST:
        request.session['font_size'] = True
    else:
        request.session['font_size'] = False
    request.session['log'].append([request.session['new_word'], request.session['color']])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
