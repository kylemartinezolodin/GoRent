from django.urls import path
from . import views

app_name='registers'
urlpatterns=[
   path('GoRentlogin/', views.GoRentLoginPage.as_view(), name="gorent_login_view"),
   path('GoRentregister/', views.GoRentRegisterPage.as_view(), name="gorent_register_view"),
]