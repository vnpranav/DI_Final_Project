from django.db import models
from django.contrib.auth.models import User
import datetime
import os

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   email = models.CharField(max_length=150, null=False)
   phone = models.CharField(max_length=150, null=False)
   address = models.TextField(max_length=600, null=False)
   city = models.CharField(max_length=150, null=False)
   state = models.CharField(max_length=150, null=False)
   country = models.CharField(max_length=150, null=False)
   zipcode = models.CharField(max_length=150, null=False)
   created_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.username
   


# Define base models such as category, brand, product, project
def get_file_path(request, file_name):
   original_filename = file_name
   time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
   file_name = f"{time_now}_{original_filename}"
   return os.path.join('uploads/', file_name)


# Create your models here.
# category model not necessary
# class Category(models.Model):
#    slug = models.CharField(max_length=150, null=False, blank=False)
#    name = models.CharField(max_length=150, null=False, blank=False)
#    description = models.TextField(max_length=500, null=False, blank=False)
#    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
#    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")

#    meta_title = models.CharField(max_length=150, null=False, blank=False)
#    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
#    meta_description = models.TextField(max_length=500, null=False, blank=False)
#    created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

class Brand(models.Model):
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   
   #meta attributes used for searching and for slugs
   #they have been added for future use or project expansion
   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

class Product(models.Model):
   brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # A product belongs to a brand
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   product_image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   short_description = models.CharField(max_length=150, null=False, blank=False)
   description = models.TextField(max_length=1000, null=False, blank=False)
   quantity = models.IntegerField(null=False, blank=False)
   selling_price = models.FloatField(null=False, blank=False)
   status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
   trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
   tag = models.CharField(max_length=150, null=False, blank=False)

   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name


class Project(models.Model):
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   project_image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   short_description = models.CharField(max_length=150, null=False, blank=False)
   description = models.TextField(max_length=1000, null=False, blank=False)
   status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
   trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
   products = models.ManyToManyField(Product, through='ProjectProduct')  # A project can have multiple products
   tag = models.CharField(max_length=150, null=False, blank=False)
   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)
   project_link = models.URLField(max_length=500, null=True, blank=True)

   def __str__(self):
      return self.name
   
class ProjectProduct(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(null=False, blank=False)  # Quantity of product for the project

   class Meta:
      unique_together = ('project', 'product')  # Ensure unique combination of project and product

   def __str__(self):
      return f'{self.project.name} - {self.product.name} (Quantity: {self.quantity})'

class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   prod_qty = models.IntegerField(null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   fname = models.CharField(max_length=150, null=False)
   lname = models.CharField(max_length=150, null=False)
   email = models.CharField(max_length=150, null=False)
   phone = models.CharField(max_length=150, null=False)
   address = models.TextField(max_length=600, null=False)
   city = models.CharField(max_length=150, null=False)
   state = models.CharField(max_length=150, null=False)
   country = models.CharField(max_length=150, null=False)
   zipcode = models.CharField(max_length=150, null=False)
   totalprice = models.FloatField(null=False)
   paymentmode = models.CharField(max_length=150, null=False)
   paymentid = models.CharField(max_length=50, null=True)
   orderstatuses = (('Pending', 'Pending'),
                    ('Shipped', 'Shipped'),
                    ('Delivered', 'Delivered'),)
   status = models.CharField(max_length=150, choices=orderstatuses, default='Pending')
   message=models.TextField(null=True)
   trackno = models.CharField(max_length=150, null=True)
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.id + " " + self.trackno
   
class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   price = models.FloatField(null=False)
   quantity = models.IntegerField(null=False)

   def __str__(self):
      return self.order.id + " " + self.order.trackno + " " + self.product.name