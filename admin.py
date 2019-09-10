from django.contrib import admin
from backend import models

# Register your models here.
admin.site.register([
    models.Profile,
    models.Product,
    models.Product_Category,
    models.Product_Review,
    models.Showcase_Images



])
