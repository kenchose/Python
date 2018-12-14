from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'form/index.html')

def process(request):
    if request.method == 'POST':
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['favorite'] = request.POST['favorite']
        request.session['comment'] = request.POST['comment']
        print 'success'
        print request.session['count']
        return redirect('/result') #changed to /results when it was '/' before
    else:
        print 'unsuccessful'
        return redirect('/')

def result(request):
    return render(request, 'form/result.html')
