# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse( 'placeholder for users to login' )

def new(request):
    return HttpResponse( 'placeholder for users to create a new user record')

def new_list(request):
    return HttpResponse('this is the main lockal url page'
)

