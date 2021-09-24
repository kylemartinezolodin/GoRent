from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
#from .forms import *
from database.models import *
from registers.controller import *

import json

	
# Create your views here.

class GoRentBillingView(View):
	def get(self, request):
		return render(request, 'gildo/Billing.html')
	def post(self, request):
		return render(request, 'gildo/Billing.html')
			

class GoRentRentingView(View):
	#declarations
	coordinates = None
	address = None
	price = None
	firstname = None
	lastname = None

	def get(self, request):
		user_object = None
		user_type = "Rentee"
		if "user_email" in request.session: # IF ACCESSED THROUGH
			user_type = request.session["user_type"]
			user_email = request.session["user_email"]
			user_password = request.session["user_password"]

			if user_type == "RentOwner":
				user_object = RentOwner.objects.filter(email = user_email)
				print("Filter result: " +str(user_object))
				
				if(user_object.count() == 1 and user_object[0].password == user_password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
					user_object = user_object[0] # EXTRAC RENTOWNER OBJECT FROM LIST
					print("User object: " +str(user_object))
				rentowner = RentOwnerRenteeRequest.objects.all()
				
				return render(request, 'gildo/search.html', context={"user":user_object, "type":user_type, "rentowner":rentowner})
			
			else:
				user_object = Sharee.objects.filter(email = user_email) 
				print("Filter result: " +str(user_object))

				if(user_object.count() == 1 and user_object[0].password == user_password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
					user_object = user_object[0] # EXTRAC RENTOWNER OBJECT FROM LIST
					print("User object: " +str(user_object))
				sharee = ShareeRenteeRequest.objects.all()
				
				return render(request, 'gildo/search.html', context={"user":user_object, "type":user_type, "sharee":sharee})
		
		return render(request, 'gildo/search.html', context={"user":user_object, "type":user_type})
	
	def post (self, request):
		print(request.body)
		json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
		coordinates = json_data['Coordinates']
		address = json_data['Address']
		price = json_data['Price']
		# json_data = json_data["data"]
		firstname = request.POST.get("firstname")
		lastname = request.POST.get("lastname")
		contactnumber = request.POST.get("contactnumber")
		print(json_data['Address'])
		
		classObj = GoRentRegisterSpace(coordinates, address, price)
		classObj.registerSpace()

		asdasd = GoRentRegisterSpace(firstname, lastname)
		asdasd.addRoommate()
		
		return render(request, 'gildo/search.html')

	# def addRoommates #add the functions from SRS

class GoRentAboutView(View):
	def get(self, request):
		return render(request, 'gildo/aboutPage.html')