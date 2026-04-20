from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def list_products(request):
 
    
    return render(request, 'products.html')
def product_detail(request, product_id):
    
    return render(request, 'product_detail.html', {'product_id': product_id})

