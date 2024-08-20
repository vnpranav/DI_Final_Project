from django.db import models
import datetime
import os

# Define base models such as category, brand, product, project
def get_file_path(request, file_name):
   original_filename = file_name
   time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
   file_name = f"{time_now}_{original_filename}"
   return os.path.join('uploads/', file_name)


# Create your models here.
class Category(models.Model):
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   description = models.TextField(max_length=500, null=False, blank=False)
   status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
   trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

class Brand(models.Model):
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   description = models.TextField(max_length=500, null=False, blank=False)
   categories = models.ManyToManyField(Category, related_name='brands')  # A brand can belong to multiple categories
   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

class Product(models.Model):
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   slug = models.CharField(max_length=150, null=False, blank=False)
   name = models.CharField(max_length=150, null=False, blank=False)
   product_image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
   short_description = models.CharField(max_length=150, null=False, blank=False)
   description = models.TextField(max_length=500, null=False, blank=False)
   quantity = models.IntegerField(null=False, blank=False)
   original_price = models.FloatField(null=False, blank=False)
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
   description = models.TextField(max_length=500, null=False, blank=False)
   status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
   trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
   products = models.ManyToManyField(Product, related_name='projects')  # A project can have multiple products
   tag = models.CharField(max_length=150, null=False, blank=False)
   meta_title = models.CharField(max_length=150, null=False, blank=False)
   meta_keywords = models.CharField(max_length=150, null=False, blank=False)
   meta_description = models.TextField(max_length=500, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name
