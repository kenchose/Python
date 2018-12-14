# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
import json

# Create your views here.
def index(request):
    if not 'words' in request.session:
        print("in the creating words of seswsion stuff")
        request.session['words'] = []

    context = {
        'words': request.session['words']
    }
    return render(request, 'words/index.html', context)

def add(request):
    new_word = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'timestamp': str(datetime.now())
    }

    print(datetime.now())

    if 'big_font' in request.POST:
        new_word['big_font'] = True
    else:
        new_word['big_font'] = False

    request.session['words'].append(new_word)
    request.session.modified = True

    return redirect('/session_words')