from django.shortcuts import render

# Create your views here.
def show_account(request):
    return render(request, "account.html")

def detail_customer(request):
    return render(request, "detail_customer.html")

