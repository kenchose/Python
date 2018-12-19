# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import *


def index(request):
    users = User.objects.all()
    context = {
        'all_users': users
    }
    return render(request, 'restful_user/index.html', context)

def new(request):
    return render(request, 'restful_user/new.html')

def add(request):
    # print (request.POST) checking to make sure the data is coming through the way we expect it to
    if request.method == 'POST':
        User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email']) #after creating test it out in the index by creating context
    return redirect('/users')

def show(request, user_id): #"user_id" var name grabbed from the urls.py
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email=request.POST['email']
        user.save()
        return redirect('/users/{}'.format(user_id))
    else:
        user = User.objects.get(id=user_id)
        context = {
            'user':  user
        }
        return render (request, 'restful_user/show.html', context)
        

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user':  user
    }
    return render (request, 'restful_user/edit.html', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')
