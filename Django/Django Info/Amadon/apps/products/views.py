# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import *


def index(request):
    products = Product.objects.all()
    context = {
        'all_products': products
    }
    return render (request, 'products/index.html', context)

def add_product(request):
    print (request.POST)
    Product.objects.create(name=request.POST['name'], price=request.POST['price'])
    return redirect ('/')

def buy(request):
    #need to get that specific product_id to know how much to charge the buyer for that product. This is by getting the id name from line 24 in buy form. so we need to create a query. the variable 'product_id is what we named the product from line 24
    product = Product.objects.get(id = request.POST['product_id'])
    
    if 'current_price' in request.session:
        request.session['current_price'] = float(product.price) * float(request.POST['quantity'])
    else:
        request.session['current_price'] = float(product.price) * float(request.POST['quantity'])

    if 'total_items' in request.session:
        request.session['total_items'] += int(request.POST['quantity']) #use int so that we can a full number when it says you have ordered a number of X items instead of you have orderd a number of X.00 items
    else:
        request.session['total_items'] = int(request.POST['quantity'])

    if 'total_spent' in request.session:
        request.session['total_spent'] += float(request.session['current_price'])
    else:
        request.session['total_spent'] = float(request.session['current_price'])     

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'products/checkout.html')