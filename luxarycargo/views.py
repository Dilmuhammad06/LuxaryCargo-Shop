from django.shortcuts import render
from django.views import View
from .models import Product, Category

class IndexView(View):
    def get(self,request):
        products = Product.objects.filter(is_available=True).order_by('-id')
        return render(request,'index.html',{"products":products})


class StoreView(View):
    def get(self,request):
        return render(request,'store.html')

class CheckoutView(View):
    def get(self,request):
        return render(request,'checkout.html')


class ProductViewView(View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        return render(request,'product.html',{"product":product})


class BlankView(View):
    def get(self,request):
        return render(request,'blank.html')
