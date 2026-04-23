from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')
def list_products(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 1)
    page_number=1
    if request.GET.get('page'):
        page_number=int(request.GET.get('page', 1))

    
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html',{'products':page_obj})
def detail_product(request):
    return render(request, 'product_detail.html')

