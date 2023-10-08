from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ProductModel)
admin.site.register(models.PersonModel)
admin.site.register(models.SellerModel)
admin.site.register(models.ClientModel)
admin.site.register(models.ComissionModel)
