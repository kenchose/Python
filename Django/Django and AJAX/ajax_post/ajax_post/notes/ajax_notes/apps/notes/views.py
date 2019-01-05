# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages
from django.core import serializers
import json 

def index(request):
    all_notes = Note.objects.all()
    context = {
        'notes': all_notes,
    }
    return render(request, 'notes/index.html', context)

def all_note(request):
    all_notes = Note.objects.all()
    context = {
        'notes': all_notes,
    }
    return render(request, 'notes/note.html', context)

def new_note(request):
    if request.method == 'POST':
        errors = []
        if (len(request.POST['note']) < 1):
            errors.append('Note title cannot be empty.')
        if (len(request.POST['description']) < 1):
            errors.append('Description title cannot be empty.')
        if errors:
            for e in errors:
                messages.error(request, e)
            return redirect('/')
        note = Note.objects.create(note=request.POST['note'], description=request.POST['description'])
        all_notes = Note.objects.all()
        context = {
            'notes': all_notes,
        }
        return render(request, 'notes/note.html', context)
    else:
        return redirect('/')

def edit(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.note = request.POST['note']
        note.description = request.POST['description']
        note.save()
        all_notes = Note.objects.all()
        context = {
            'notes': all_notes,
        }
        return redirect ('/')
    else:
        return redirect('/')

def delete(request, note_id):
    note = Note.objects.get(id=note_id).delete()
    return redirect ('/')

        

