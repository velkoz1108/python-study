from django.contrib import admin

# Register your models here.
from Product.models import Product, proft

admin.site.register([Product, proft])
