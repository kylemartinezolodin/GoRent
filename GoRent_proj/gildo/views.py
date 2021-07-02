from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
	
# Create your views here.

class GoRentBillingView(View):
	def get(self, request):
		return render(request, 'gildo/Billing.html')
	def post(self, request):
		return render(request, 'gildo/Billing.html')
			

class GoRentRentingView(View):
	def get(self, request):
		return render(request, 'gildo/search.html')
		