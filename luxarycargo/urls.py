from django.urls import path
from .import views

urlpatterns = [
    path("",views.IndexView.as_view(), name='home'),
    path("store/",views.StoreView.as_view(), name="store"),
    path("checkout/",views.StoreView.as_view(), name="checkout"),
    path("product/<int:id>/",views.ProductViewView.as_view(), name="product"),
    path("blank/",views.BlankView.as_view(), name="blank")
]
