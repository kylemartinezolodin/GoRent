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
		user_object = None

		if "user_email" in request.session: # IF ACCESSED THROUGH
			user_email = request.session["user_email"]
			user_password = request.session["user_password"]

			user_object = RentOwner.objects.filter(email = user_email) 
			print("Filter result: " +str(user_object))

			if(user_object.count() == 1 and user_object[0].password == user_password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
				user_object = user_object[0] # EXTRAC RENTOWNER OBJECT FROM LIST
				print("User object: " +str(user_object))

		return render(request, 'gildo/search.html', context={"user":user_object})

		