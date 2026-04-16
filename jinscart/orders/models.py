from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    LIVE=1
    DELETED=0
    DELETED_CHOICES=(
        (LIVE,'Live'), 
        (DELETED,'Deleted'))
    CART_STAGE=0
    ORDER_CONFIRMED_STAGE=1
   
    ORDER_PROCESSING_STAGE=2
    ORDER_DELIVERED_STAGE=3
    ORDER_REJECTED_STAGE=4

    STATUS_CHOICES=(
        

        (ORDER_REJECTED_STAGE,'Order Rejected'),
        (ORDER_PROCESSING_STAGE,'Order Processing'),
        (ORDER_DELIVERED_STAGE,'Order Delivered')   
    )


    order_status= models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE) 
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,related_name='orders', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_status=models.IntegerField(choices=DELETED_CHOICES,default=LIVE)

    def __str__(self):
        return f"Order {self.id} for {self.owner.name}"
class OrderedItem(models.Model):
  
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,related_name='added_carts')
    quantity = models.PositiveIntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.owner.id}"
    



