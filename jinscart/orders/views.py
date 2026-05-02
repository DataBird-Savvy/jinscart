from django.shortcuts import render, redirect
from .models import Order, OrderedItem
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product
from django.contrib import messages
# Create your views here.
def show_orders(request):
    user=request.user
    customer= user.customer_profile
    order_obj,created=Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
    context={
        'cart':order_obj
    }

    return render(request, "cart.html", context)

def add_to_cart(request):
    if request.method == "POST":
        user=request.user
        customer= user.customer_profile
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        order_obj,created=Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
        product=Product.objects.get(id=product_id)
        ordered_item_obj,created=OrderedItem.objects.get_or_create(order=order_obj, product=product)
        if created:
            ordered_item_obj.quantity = quantity
            ordered_item_obj.save()
        else:
            ordered_item_obj.quantity = ordered_item_obj.quantity + quantity
            ordered_item_obj.save()
   
    return redirect('cart')

def checkout_cart(request):
    try:
        user=request.user
        customer= user.customer_profile
        total=float(request.POST.get("total"))
        order_obj=Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
        
        if order_obj:
            order_obj.order_status=Order.ORDER_CONFIRMED_STAGE
            order_obj.save()
            messages.success(request, "Your order has been placed successfully!")
        else:
            messages.error(request, "There was an error processing your order. Please try again.")
        return redirect('cart')
    except Exception as e:
        messages.error(request, "An unexpected error occurred. Please try again.")
    return redirect('cart')

def remove_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')