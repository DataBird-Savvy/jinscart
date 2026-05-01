from django.shortcuts import render, redirect
from .models import Order, OrderedItem
# Create your views here.
def show_orders(request):
    return render(request, "cart.html")

def add_to_cart(request):
    if request.method == "POST":
        user=request.user
        customer=user.customer_profile
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        order_obj,created=Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
        ordered_item_obj,created=OrderedItem.objects.create(order=order_obj, product_id=product_id, quantity=quantity)
   
    return render(request, "cart.html")