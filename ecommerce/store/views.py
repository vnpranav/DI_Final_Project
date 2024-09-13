from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
   
def project_detail(request, slug):
    # Retrieve the project by slug
    project = get_object_or_404(Project, slug=slug)
    
    # Retrieve the products and their quantities for this project
    project_products = ProjectProduct.objects.filter(project=project)
    
    context = {
        'project': project,
        'project_products': project_products,
    }
    
    return render(request, 'store/project_detail.html', context)

def project_list(request):
    # Fetch all projects
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    
    return render(request, 'store/project_list.html', context)

@login_required(login_url='loginpage')
def add_project_to_cart(request, slug):
    if request.method == 'POST':
        # Get the project based on slug
        project = get_object_or_404(Project, slug=slug)
        
        # Get all project products with their quantities
        project_products = ProjectProduct.objects.filter(project=project)
        
        # Check if there are any products in the project
        if not project_products.exists():
            return redirect('project_detail', slug=slug)  # Redirect if no products found
        
        # Iterate over the products in the project and add each one to the cart
        for project_product in project_products:
            product = project_product.product
            product_qty = project_product.quantity
            
            # Check if the product has enough stock
            if product.quantity >= product_qty:
                # Check if the product is already in the user's cart
                cart_item, created = Cart.objects.get_or_create(
                    user=request.user, product=product,
                    defaults={'prod_qty': product_qty}
                )
                
                # If the item is already in the cart, you can update its quantity
                if not created:
                    cart_item.prod_qty += product_qty
                    cart_item.save()

               
            else:
                # Redirect to project details page with a message
                return redirect('project_detail', slug=slug)  # Redirect with a message can be added here
        
        # Redirect to a confirmation page or back to the project details
        return redirect('project_detail', slug=slug)

    return redirect('project_detail', slug=slug)  # Redirect if not POST request