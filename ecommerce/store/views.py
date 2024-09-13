from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
   trending_products = Product.objects.filter(trending=1)
   context = {'trending_products': trending_products}
   return render(request, 'store/index.html', context=context)

def brands(request):
   brand_list = Brand.objects.all()
   context = {'brands' : brand_list}
   print(context)
   return render(request, 'store/brands.html', context)

def brand_view(request, slug):
   if (Brand.objects.filter(slug=slug)):
      products = Product.objects.filter(brand__slug=slug)
      brand = Brand.objects.filter(slug=slug).first()
      context = {'products' : products, "brand" : brand }
      return render(request, 'store/products/index.html', context)
   else:
      messages.warning(request, "No such brand or products found")
      return redirect('brands')
   
def product_view(request, brand_slug, prod_slug):
   if (Product.objects.filter(slug=prod_slug, brand__slug=brand_slug, status=0)):
      product = Product.objects.filter(slug=prod_slug, brand__slug=brand_slug).first()
      context = {'product' : product }
      return render(request, 'store/products/product.html', context)
   else:
      messages.warning(request, "No such product found")
      return redirect('brands')
   
def productlist(request):
   products = Product.objects.filter(status=0).values_list('name', flat=True)
   prodlist = list(products)

   return JsonResponse(prodlist, safe=False)

def searchproduct(request):
   if request.method == 'POST':
      searchtarget = request.POST.get('search')
      
      if searchtarget == "":
         return redirect(request.META.get("HTTP_REFERER"))
      else:
         product = Product.objects.filter(name__icontains=searchtarget, status=0).first()

         if product:
            return redirect('product_view', brand_slug=product.brand.slug, prod_slug=product.slug)
         else:
            messages.warning(request, "No such product found")
            return redirect(request.META.get("HTTP_REFERER"))

   
   else:
      return redirect(request.META.get("HTTP_REFERER"))
