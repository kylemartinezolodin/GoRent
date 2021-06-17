from django.urls import path
from . import views

app_name='sharee'
urlpatterns=[
   path('', views.ShareeLandingPage.as_view(), name="sharee_landing_view"),
]