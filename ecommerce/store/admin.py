from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(ProjectProduct)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)