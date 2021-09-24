from django.urls import path
from . import views

app_name='registers'
urlpatterns=[
   path('Owner/Login', views.GoRentLoginOwnerPage.as_view(), name="loginOwner_view"),
   path('Sharee/Login', views.GoRentLoginShareePage.as_view(), name="loginSharee_view"),
   path('Owner/Register', views.GoRentOwnerRegisterPage.as_view(), name="OwnerRegister_view"),
   path('Sharee/Register', views.GoRentShareeRegisterPage.as_view(), name="ShareeRegister_view"),
   path('', views.GoRentAboutPage.as_view(), name="about_view"),
   
   path('Logout', views.GoRentLogoutPage.as_view(), name="logout_view"),
]