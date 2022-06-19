from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
#from .forms import *
from database.models import *
from .controller import *
import json
	
# Create your views here.

class GoRentBillingView(View):
	def get(self, request):
		return render(request, 'gildo/Billing.html')
	def post(self, request):
		return render(request, 'gildo/Billing.html')
			

class GoRentMainView(View):
	def get(self, request):
		user_object = None
		user_type = "Rentee"
		user_email = None
		user_password = None
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
		
	def post(self, request):
		if request.method == 'POST':
			print("hello")
			request = json.loads(request.body)
			print(request)
			if request["ajaxAction"] == "getNearbySpaces":
				user_coord = [request["latitude"],["longitude"]]
				classObject = GoRentNearbySpace(request["latitude"], request["longitude"])
				nearby_spaces = classObject.rankSpaces()

				print(nearby_spaces)
				return JsonResponse({'nearby_spaces':nearby_spaces})
			elif request["ajaxAction"] == "renteeApplicationSubmition":
				print("duka")
				print(request["owner"])
				print(request["email"])
				return JsonResponse({})
				# save RentOwnerRenteeRequest data 
		else:
			if 'btnAccept' in request.POST:
				print("accept button clicked")
				eid = request.POST.get("email-id")
				em = Sharee.objects.filter(email_ptr_id=eid).delete()
				perss = ShareeRenteeRequest.objects.filter(id = eid).delete()
				print('record deleted')

			elif 'btnDelete' in request.POST:
				print("delete button clicked")
				eid = request.POST.get("email-id")
				em = Sharee.objects.filter(email_ptr_id=eid).delete()
				pers = ShareeRenteeRequest.objects.filter(id = eid).delete()
				print('record deleted')

		return redirect('gildo/search.html')
		
		# nearby = json.loads(request.body)
		# print(nearby["longitude"])
		# return JsonResponse({'foo':'bar'})