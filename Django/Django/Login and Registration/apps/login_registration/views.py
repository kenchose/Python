from __future__ import unicode_literals
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import bcrypt
from datetime import date, datetime
from django.contrib.auth import logout
from datetime import date
from django.shortcuts import render

def index(request):
    return render (request, 'login_registration/index.html')

def process(request):
    if request.method == 'POST':
        errors = []
        for key, val in request.POST.items():
            if len(val) < 1:
                errors.append('{} field must be filled in.'.format(key))
        if (len(request.POST['first_name']) < 2):
            errors.append('First name must be more than 2 characters.')
        if (len(request.POST['last_name']) < 2):
            errors.append('Last name must be more than 2 characters.')
        if (len(request.POST['email']) < 6):
            errors.append('Email must be at least 6 characters long')
        try:
            validate_email(request.POST['email'])
        except ValidationError as e:
            errors.append('Email must be a valid email.')
        if (len(request.POST['password']) < 8):
            errors.append('Password must be at least 8 characters.')
        if request.POST['password'] != request.POST['password_confirmation']:
            errors.append('Password and confirmation password must match.')
        if errors:
            for e in errors:
                messages.error(request, e)
            return redirect('/')
        else:
            try:
                User.objects.get(email=request.POST['email'])
                messages.error(request, 'Email already/does not exist please try again.')
                return redirect ('/')
            except User.DoesNotExist:
                hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                
                user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)

                request.session['id'] = user.id  
                return redirect('/success') 
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email']) 
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()): 
                request.session['id'] = user.id 
                return redirect ('/success')
            else:
                messages.error(request, "Email or passowrd do not match")
                return redirect('/')
        except User.DoesNotExist:
            messages.error(request, "Email does not exist.")
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    if not 'id' in request.session:
        redirect ('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        'user':user,
    }
    return render (request, 'login_registration/success.html', context)


def logout(request):
    request.session.clear()
    return redirect('/')

