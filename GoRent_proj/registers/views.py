from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
	
# Create your views here.

class GoRentLoginOwnerPage(View):
	def get(self, request):
		return render(request, 'registers/loginOwner.html')
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginOwner' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user_object = RentOwner.objects.filter(email = username)
				if(user_object.count() == 1 and user_object[0].password == password):
					return HttpResponse("Success") #PUT THE REDIRECTORY FOR THE OWNER MAINPAGE HERE
				else:
					return HttpResponse("Fail")

class GoRentLoginShareePage(View):
	def get(self, request):
		return render(request, 'registers/loginSharee.html')
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginSharee' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user_object = Sharee.objects.get(email = username)
				if(user_object.count() == 1 and user_object[0].password == password):
					return HttpResponse("Success") #PUT THE REDIRECTORY FOR THE SHAREE MAINPAGE HERE
				else:
					return HttpResponse("Fail")


class GoRentOwnerRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html')
	def post (self,request):
		firstName = request.POST.get("firstName")
		lastName = request.POST.get("lastName")
		email = request.POST.get("email")
		password = request.POST.get("password")
		mobileNumber = request.POST.get("mobileNumber")
		birthdate = request.POST.get("birthdate")
		
		obj = RentOwner(email = email, firstname = firstName, lastname = lastName, password = password, contactnumber = mobileNumber, 
			birthday = birthdate)
		obj.save()
		return render(request, 'registers/loginOwner.html')

class GoRentShareeRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html')
	def post (self,request):
		shareeFirstName = request.POST.get("firstName")
		shareeLastName = request.POST.get("lastName")
		shareeEmail = request.POST.get("email")
		shareePassword = request.POST.get("password")
		shareeMobileNumber = request.POST.get("mobileNumber")
		shareeBirthdate = request.POST.get("birthdate")
		
		obj = Sharee(email = shareeEmail, firstname = shareeFirstName, lastname = shareeLastName, password = shareePassword, contactnumber = shareeMobileNumber, 
			birthday = shareeBirthdate)
		obj.save()
		return redirect('registers:gorent_loginSharee_view')

class GoRentLandingPage(View):
	def get(self, request):
		return render(request, 'registers/landingPage.html')
		