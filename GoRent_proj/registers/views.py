from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
	
# Create your views here.

class GoRentLoginOwnerPage(View):
	def get(self, request):
		return render(request, 'registers/loginOwner.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE

	def post(self, request):
		username = request.POST.get("username")
		password = request.POST.get("password")

		user_object = RentOwner.objects.filter(email = username) 
		print(user_object)

		if(user_object.count() == 1 and user_object[0].password == password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
			user_object = user_object[0]

			# USING REDIRECT DOES NOT HAVE CONTEXT ARGUMENT THUS WE NEED TO USE SESSIONS
			request.session["user_email"] = user_object.email
			request.session["user_password"] = user_object.password

			return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)

		else:
			return HttpResponse("Fail \n inputs: " +username +", " +password +" Para rani debug dapat jud dili maka hibaw ang mo login unsa iya sayup")

class GoRentLoginShareePage(View):
	def get(self, request):
		return render(request, 'registers/loginSharee.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginSharee' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user_object = Sharee.objects.get(email = username)
				if(user_object.count() == 1 and user_object[0].password == password):  # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
					
					return HttpResponse("Success") #PUT THE REDIRECTORY FOR THE SHAREE MAINPAGE HERE
				else:
					return HttpResponse("Fail \n inputs: " +username +", " +password +" Para rani debug dapat jud dili maka hibaw ang mo login unsa iya sayup")


class GoRentOwnerRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post (self,request):
		firstName = request.POST.get("firstName")
		lastName = request.POST.get("lastName")
		email = request.POST.get("email")
		password = request.POST.get("password")
		mobileNumber = request.POST.get("mobileNumber")
		birthdate = request.POST.get("birthdate")
		occupation = request.POST.get("occupation")
		
		obj = RentOwner(email = email, firstname = firstName, lastname = lastName, password = password, contactnumber = mobileNumber, birthday = birthdate, occupation = occupation)
		obj.save()
		return render(request, 'registers/loginOwner.html')

class GoRentShareeRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post (self,request):
		shareeFirstName = request.POST.get("firstName")
		shareeLastName = request.POST.get("lastName")
		shareeEmail = request.POST.get("email")
		shareePassword = request.POST.get("password")
		shareeMobileNumber = request.POST.get("mobileNumber")
		shareeBirthdate = request.POST.get("birthdate")
		
		obj = Sharee(email = shareeEmail, firstname = shareeFirstName, lastname = shareeLastName, password = shareePassword, contactnumber = shareeMobileNumber, birthday = shareeBirthdate)
		obj.save()
		return render(request, 'registers/loginSharee.html')# BAWAL

class GoRentLogoutPage(View):
	def get(self, request):
		request.session.clear()
		request.session.flush()
		return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)
		