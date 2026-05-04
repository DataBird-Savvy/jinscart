from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show_account(request):
    context = {}
    if request.method == "POST" and 'register' in request.POST:
        context['register'] = True
        try:
            print(request.POST) 
    
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            print(username, password, email, address, phone)

            if User.objects.filter(username=username).exists():
                error_message = "Username already exists"
                messages.error(request, error_message)
                return render(request, "account.html", context)

            user = User.objects.create_user(username=username, password=password, email=email)

          
            customer = Customer(user=user, address=address, phone_number=phone,name=username)
            customer.save()
           
            messages.success(request, "Registration successful. Please log in.")
        except Exception as e:
            error_message= str(e)
            messages.error(request, error_message)

    if request.method == "POST" and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "account.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')

def detail_customer(request):
    return render(request, "detail_customer.html")

