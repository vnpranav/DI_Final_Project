from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from store.models import Cart, Order, OrderItem, Product, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

@login_required(login_url="loginpage")
def index(request):
   rawcart = Cart.objects.filter(user=request.user)
   for item in rawcart:
      if item.prod_qty > item.product.quantity:
         Cart.objects.delete(id=item.id)
   
   cartitems = Cart.objects.filter(user=request.user)
   totalprice = 0
   for item in cartitems:
      totalprice += item.product.selling_price * item.prod_qty

   userprofile = Profile.objects.filter(user=request.user).first()

   context = {'cartitems': cartitems, 'total': totalprice, 'userprofile' : userprofile}
   return render(request, 'store/checkout.html', context)

@login_required(login_url="loginpage")
def placeorder(request):
   if request.method == 'POST':
         
         currentuser = User.objects.filter(id=request.user.id).first()
         if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
         
         if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.zipcode = request.POST.get('zip')
            userprofile.save()

         neworder = Order()
         neworder.user = request.user
         neworder.fname = request.POST.get('fname')
         neworder.lname = request.POST.get('lname')
         neworder.email = request.POST.get('email')
         neworder.phone = request.POST.get('phone')
         neworder.address = request.POST.get('address')
         neworder.city = request.POST.get('city')
         neworder.state = request.POST.get('state')
         neworder.zipcode = request.POST.get('zip')
         neworder.paymentmode = request.POST.get('payment_mode')

         carts = Cart.objects.filter(user=request.user)
         total = 0
         for item in carts:
            total += item.product.selling_price * item.prod_qty
         
         neworder.totalprice = total

         trackno = request.user.username + str(random.randint(111111,999999))
         while Order.objects.filter(trackno=trackno) is None:
            trackno = request.user.username + str(random.randint(111111,999999))
         neworder.trackno = trackno
         neworder.save()

         neworderitems = Cart.objects.filter(user=request.user)
         for item in neworderitems:
            OrderItem.objects.create(
               order=neworder,
               product=item.product,
               price = item.product.selling_price,
               quantity = item.prod_qty
            )

            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity -= item.prod_qty
      
            orderproduct.save()

         Cart.objects.filter(user=request.user).delete()

         messages.success(request, "Order placed successfully")
         return redirect("/orders")
   else:
      return redirect("/")

