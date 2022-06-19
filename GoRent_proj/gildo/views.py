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
	user_object = None
	user_type = "Rentee"

	user_email = None
	user_password = None

	def get(self, request):
		if "user_email" in request.session: # IF ACCESSED THROUGH
			self.user_type = request.session["user_type"]
			self.user_email = request.session["user_email"]
			self.user_password = request.session["user_password"]

			if self.user_type == "RentOwner":
				self.user_object = RentOwner.objects.filter(email = self.user_email)
				print("Filter result: " +str(self.user_object))
				
				if(self.user_object.count() == 1 and self.user_object[0].password == self.user_password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
					self.user_object = self.user_object[0] # EXTRAC RENTOWNER OBJECT FROM LIST
					print("User object: " +str(self.user_object))

				rentowner = RentOwnerRenteeRequest.objects.all()
				
				return render(request, 'gildo/search.html', context={"user":self.user_object, "type":self.user_type, "rentowner":rentowner})
			
			else:
				self.user_object = Sharee.objects.filter(email = self.user_email) 
				print("Filter result: " +str(self.user_object))

				if(self.user_object.count() == 1 and self.user_object[0].password == self.user_password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
					self.user_object = self.user_object[0] # EXTRAC RENTOWNER OBJECT FROM LIST
					print("User object: " +str(self.user_object))
				sharee = ShareeRenteeRequest.objects.all()
				
				return render(request, 'gildo/search.html', context={"user":self.user_object, "type":self.user_type, "sharee":sharee})
		
		return render(request, 'gildo/search.html', context={"user":self.user_object, "type":self.user_type})
		
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