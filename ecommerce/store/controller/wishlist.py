from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Wishlist, Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
   wishlist_items = Wishlist.objects.filter(user=request.user)
   context = {'wishlist' : wishlist_items}
   return render(request, 'store/wishlist.html', context=context)

def addtowishlist(request):
   if request.method == 'POST':
      if request.user.is_authenticated:
         product_id = request.POST['prod_id']
         product_check= Product.objects.get(id=product_id)

         if(product_check):
            wishlist = Wishlist.objects.filter(user=request.user, product=product_check)
            if wishlist.exists():
               return JsonResponse({'status' : 'Product already exists in your wishlist'})
            else:
               wishlist = Wishlist(user=request.user, product=product_check)
               wishlist.save()
               return JsonResponse({'status' : 'Product added to wishlist'})
         else:
            return JsonResponse({'status' : 'Product not found'})
      else:
         return JsonResponse({'status' : 'You must be logged in to add product to wishlist'})
      
   return redirect("/")

def deleteitem(request):
   if request.method == 'POST':
      if request.user.is_authenticated:
         product_id = int(request.POST['prod_id'])

         wishlist = Wishlist.objects.filter(user=request.user, product_id=product_id)
         if wishlist.exists():
               wishlist.delete()
               return JsonResponse({'status' : 'Product removed from your wishlist'})
         else:
               return JsonResponse({'status' : 'Product not found wishlist'})

      else:
         return JsonResponse({'status' : 'You must be logged in to add product to wishlist'})
      
   return redirect("/")

