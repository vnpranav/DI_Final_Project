from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from store.models import Cart, Order, OrderItem, Product, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

@login_required(login_url="loginpage")
def index(request):
   orders = Order.objects.filter(user=request.user)
   context = {'orders' : orders}
   return render(request, 'store/order/orders.html', context)

def orderview(request, t_no):
   order = Order.objects.filter(trackno=t_no).filter(user=request.user).first()
   orderitems = OrderItem.objects.filter(order=order)
   context = {'order' : order, 'orderitems' : orderitems}
   return render(request, 'store/order/orderview.html', context)