from django.urls import path
from . import views

app_name='registers'
urlpatterns=[
   path('GoRentloginOwner/', views.GoRentLoginOwnerPage.as_view(), name="gorent_loginOwner_view"),
   path('GoRentloginSharee/', views.GoRentLoginShareePage.as_view(), name="gorent_loginSharee_view"),
   path('GoRentOwnerRegister/', views.GoRentOwnerRegisterPage.as_view(), name="gorent_OwnerRegister_view"),
   path('GoRentShareeRegister/', views.GoRentShareeRegisterPage.as_view(), name="gorent_ShareeRegister_view"),
   path('GoRentlanding/', views.GoRentLandingPage.as_view(), name="gorent_landing_view"),
]