from django.contrib import admin
from .models import Product, Size, Category, Color

admin.site.register([Size, Product, Category, Color])