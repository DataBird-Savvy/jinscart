from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    featured_product=Product.objects.order_by('-priority')[:4]
    latest_product=Product.objects.order_by('-id')[:4]
    context={
        'featured_product':featured_product,
        'latest_product':latest_product
    }
    return render(request, 'index.html', context)
def list_products(request):
    
    page_number=1
    if request.GET.get('page'):
        page_number=int(request.GET.get('page', 1))
    product_list=Product.objects.order_by('-priority')
    paginator = Paginator(product_list, 1)
    
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html',{'products':page_obj})
def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

