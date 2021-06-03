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
			return redirect('#') #put the redirecttory for the mainpage for Owners here

class GoRentLoginShareePage(View):
	def get(self, request):
		return render(request, 'registers/loginSharee.html')
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginSharee' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
			return redirect('#') #put the redirecttory for the mainpage for Sharee here

class GoRentOwnerRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html')
	def post (self,request):
		ownerFirstName = request.POST.get("firstname")
		ownerLastName = request.POST.get("lastname")
		ownerEmail = request.POST.get("email")
		ownerPassword = request.POST.get("password")
		ownerMobileNumber = request.POST.get("contactnumber")
		ownerBirthdate = request.POST.get("birthdate")
		
		obj = GoRentOwner(email = ownerEmail, firstname = ownerFirstName, lastname = ownerLastName, password = ownerPassword, contactnumber = ownerMobileNumber, 
			birthdate = ownerBirthdate)
		obj.save()
		return redirect('registers: gorent_loginOwner_view')

class GoRentShareeRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html')
	def post (self,request):
		shareeFirstName = request.POST.get("firstname")
		shareeLastName = request.POST.get("lastname")
		shareeEmail = request.POST.get("email")
		shareePassword = request.POST.get("password")
		shareeMobileNumber = request.POST.get("contactnumber")
		shareeBirthdate = request.POST.get("birthdate")
		
		obj = GoRentSharee(email = shareeEmail, firstname = shareeFirstName, lastname = shareeLastName, password = shareePassword, contactnumber = shareeMobileNumber, 
			birthdate = shareeBirthdate)
		obj.save()
		return redirect('registers: gorent_loginSharee_view')

class GoRentLandingPage(View):
	def get(self, request):
		return render(request, 'registers/landingPage.html')
		