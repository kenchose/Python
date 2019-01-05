# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from . models import *
from django.core import serializers
import json

def index (request):
    context = {
        "all_notes": Note.objects.all()
    }
    return render(request, 'notes/index.html', context)

def add_note (request):
    note = Note.objects.create(note=request.POST['note'])
    context = {
        'new_note': note,
        'all_notes': Note.objects.all()
    }
    return render (request, 'notes/new_note.html', context)

