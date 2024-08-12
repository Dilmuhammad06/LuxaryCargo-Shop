from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.size} size'
    
class Color(models.Model):
    color = models.CharField(max_length=255)
    
    def __str__(self):
        return self.color
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    size = models.ManyToManyField(Size, related_name="products")
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} costs {self.price}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    total_price = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ordered {self.order_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.quantity}'