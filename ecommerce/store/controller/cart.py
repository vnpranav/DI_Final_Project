from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Product, Cart
from django.contrib.auth.decorators import login_required

def addtocart(request):
   if request.method == 'POST':
      if request.user.is_authenticated:
         product_id = int(request.POST.get('prod_id'))
         product_check = Product.objects.get(id=product_id)

         if(product_check):
            if (Cart.objects.filter(user=request.user.id, product_id=product_id)):
               return JsonResponse ({'status' : 'Product already in cart'})
            else:
               product_qty = int(request.POST.get('prod_qty'))
               if product_check.quantity >= product_qty:
               # create cart object
                  Cart.objects.create(user=request.user, product_id=product_id, prod_qty=product_qty)
                  return JsonResponse ({'status' : 'Product added in cart'})
               else:
                  return JsonResponse ({'status' : 'Product quantity is not available'})
         else:
            return JsonResponse ({'status' : 'Product not found'})
      else:
         return JsonResponse({'status' : 'User not authenticated'})

   return redirect("/index")

@login_required(login_url='loginpage')
def cart(request):
   carts = Cart.objects.filter(user=request.user)
   context = {'cart' : carts}
   return render(request,"store/cart.html", context)


def updatecart(request):
   if request.method == 'POST':
      product_id = int(request.POST.get('prod_id'))
      if(Cart.objects.filter(user=request.user, product_id=product_id)):
         product_qty = int(request.POST.get('prod_qty'))
         cart = Cart.objects.get(product_id=product_id, user=request.user)
         cart.prod_qty = product_qty
         cart.save()
         return JsonResponse({'status' : 'Product quantity updated'})
   else:
      return redirect("/index")
   

def removecart(request):
   if request.method == 'POST':
      product_id = int(request.POST.get('prod_id'))
      if(Cart.objects.filter(user=request.user, product_id=product_id)):
         cart = Cart.objects.get(product_id=product_id, user=request.user)
         cart.delete()
         return JsonResponse({'status' : 'Product removed from cart'})
      else:
         return JsonResponse({'status' : 'Product not found in cart'})
   return redirect("/index")

