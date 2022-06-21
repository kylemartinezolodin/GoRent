from django.urls import path
from . import views

app_name='gildo'
urlpatterns=[
   path('Billing', views.GoRentBillingView.as_view(), name="gorent_Billing_view"),
   path('', views.GoRentRentingView.as_view(), name="gorent_main_view"),

]