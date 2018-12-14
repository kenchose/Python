# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime


# Create your views here.

def index(request):
    return render(request, 'ninja_money/index.html')

def login(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['gold'] = 0
        request.session['events'] = []
        return redirect ('/')
    else:
        return redirect ('/')

def process(request, location):
    if request.method == 'POST':
        if location == 'farm':
            amt = random.randint(10, 20)
            event = "Earned {} gold from {} @ {}".format(amt, location, datetime.datetime.now().strftime('%M %D %Y'))
        elif location == 'cave':
            amt = random.randint(5, 10)
            event = "Earned {} gold from {} @ {}".format(amt, location, datetime.datetime.now().strftime('%M %D %Y'))
        elif location == 'house':
            amt = random.randint(2, 5)
            event = "Earned {} gold from {} @ {}".format(amt, location, datetime.datetime.now().strftime('%M %D %Y'))
        elif location == 'casino': 
            amt = random.randint(-50, 50)
            if amt >= 0:
                event = "Earned {} gold from {} @ {}".format(amt, location, datetime.datetime.now().strftime('%M %D %Y'))
            else:
                event = "Lost {} gold from {} @ {}".format(amt, location, datetime.datetime.now().strftime('%M %D %Y'))
        else:
            return redirect ('/')
        
        request.session['gold'] += amt
        curr_events = request.session['events']
        curr_events.append(event)
        request.session['events'] = curr_events
        return redirect('/')
    else:
        return redirect('/')
