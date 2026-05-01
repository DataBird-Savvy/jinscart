from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path("account", views.show_account, name="account"),
    path("logout", views.logout_view, name="logout"),
    path("customer_detail", views.detail_customer, name="detail_customer")
]
    