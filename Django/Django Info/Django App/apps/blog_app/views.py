# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('Placeholder to later display all the list of blogs')

def new(request):
    return HttpResponse('Placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse("Placeholder to display blog {}".format(number))

def edit(request, word):
    return HttpResponse('Placeholder to edit blog {}'.format(word))

def destroy(request):
    return redirect('/')