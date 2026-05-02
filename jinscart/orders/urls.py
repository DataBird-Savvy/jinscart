from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path("cart", views.show_orders, name="cart"),
    path("add-to-cart", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout", views.checkout_cart, name="checkout")
]
    