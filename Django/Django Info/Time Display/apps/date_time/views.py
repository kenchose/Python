# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import localtime, now
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {
        'time': localtime(now())
    }
    return render(request, 'date_time/index.html', context)

#changed TIME_ZONE = 'US/Pacific' in settings including importing all the localtime, now