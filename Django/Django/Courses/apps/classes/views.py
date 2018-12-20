# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import *

def index(request):
    new_course = Course.objects.all()
    context = {
        'all_courses': new_course
    }
    return render(request, 'classes/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'classes/delete.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
    