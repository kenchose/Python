# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
    return render(request, 'generate/index.html')

def random_word(request):
    if request.method == 'POST':
        request.session['attempt'] += 1
        request.session['string'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    if request.session['attempt'] > 1:
        request.session['attempt'] = 0
    return redirect ('/')

