from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
from django.http import JsonResponse
import json
from .controller import *
# Create your views here.

class GoRentLoginOwnerPage(View):
	username = None
	password = None

	def get(self, request):
		return render(request, 'registers/loginOwner.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE

	def post(self, request):
		self.username = request.POST.get("username")
		self.password = request.POST.get("password")

		ikawBahalaSaimoVariable = GoRentLogin()
		isCredentialsValid, user = ikawBahalaSaimoVariable.credentialsValidation(user_type = "RentOwner",username = self.username, password = self.password)
		print(user)

		if isCredentialsValid:
		
			# USING REDIRECT DOES NOT HAVE CONTEXT ARGUMENT THUS WE NEED TO USE SESSIONS
			request.session["user_type"] = "RentOwner"
			request.session["user_email"] = user.email
			request.session["user_password"] = user.password

			return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)

		else:
			# return HttpResponse("Fail \n inputs: " +username +", " +password +" Para rani debug dapat jud dili maka hibaw ang mo login unsa iya sayup")
			 return render(request, 'registers/loginOwner.html', {'popUpFlag':True})
			# return JsonResponse(errorMessage)

class GoRentLoginShareePage(View):
	username = None
	password = None
	def get(self, request):
		return render(request, 'registers/loginSharee.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post(self, request):

		self.username = request.POST.get("username")
		self.password = request.POST.get("password")
		user_object = Sharee.objects.filter(email = username) 
		print(user_object)
		
		if(user_object.count() == 1 and user_object[0].password == password): # THIS KIND OF VALIDATION IS APPLICABLE WHEN USING objects.filter()
			user_object = user_object[0]

			# USING REDIRECT DOES NOT HAVE CONTEXT ARGUMENT THUS WE NEED TO USE SESSIONS
			request.session["user_type"] = "Sharee"
			request.session["user_email"] = user_object.email
			request.session["user_password"] = user_object.password

			return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)

		else:
			# return HttpResponse("Fail \n inputs: " +username +", " +password +" Para rani debug dapat jud dili maka hibaw ang mo login unsa iya sayup")
			 return render(request, 'registers/loginSharee.html', {'popUpFlag':True})
			# return JsonResponse(errorLoginSharee)

class GoRentOwnerRegisterPage(View):	
	firstName = None
	lastName = None
	email = None
	password = None
	mobileNumber = None
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 

	def post (self,request):

		print(request.headers)
		print(str(request) + "asdadads")
		registerController = GoRentRegister()
		if 'application/x-www-form-urlencoded; charset=UTF-8' in request.headers["Content-Type"]:
			request = json.loads(request.body)
			if request['ajaxAction'] == 'validateEmail':
				emailData = {'error_code': registerController.emailValidator(request["checkemail"])}
				return JsonResponse(emailData)
		else:
			self.firstname = request.POST.get("firstName")
			self.lastname = request.POST.get("lastName")
			self.email = request.POST.get("email")
			self.password = request.POST.get("password")
			self.mobileNumber = request.POST.get("mobileNumber")
			birthdate = request.POST.get("birthdate")
			occupation = request.POST.get("occupation")

			obj = RentOwner(email = self.email, firstname = self.firstname, lastname = self.lastname, password = self.password, contactnumber = self.mobileNumber)
			obj.save()
			return redirect('registers:loginOwner_view')

class GoRentShareeRegisterPage(View):
	firstName = None
	lastName = None
	email = None
	password = None
	mobileNumber = None
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post (self,request):
		print(request.headers)
		print(str(request) + "asdadads")
		if 'application/x-www-form-urlencoded; charset=UTF-8' in request.headers["Content-Type"]:
			request = json.loads(request.body)
			shareeEmailData = {'is_shareeTaken': Sharee.objects.filter(email=request["checkemail"]).exists()}
			shareeEmailData['error_messageEmail'] = 'A user with this email already exists.'	
			return JsonResponse(shareeEmailData)
		else:
			self.firstname = request.POST.get("firstName")
			self.lastname = request.POST.get("lastName")
			self.email = request.POST.get("email")
			self.password = request.POST.get("password")
			self.mobileNumber = request.POST.get("mobileNumber")
			shareeBirthdate = request.POST.get("birthdate")
			
			# shareeEmailData = {'is_shareeTaken': Sharee.objects.filter(email=shareeEmail).exists()}
			# shareeEmailData['error_shareeEmail'] = 'A user with this email already exists.'
			# if shareeEmailData['is_shareeTaken']:
			# 	return JsonResponse(shareeEmailData)
			# else:
			obj = Sharee(email = self.email, firstname = self.firstname, lastname = self.lastname, password = self.password, contactnumber = self.mobileNumber)
			obj.save()
			return redirect('registers:loginSharee_view')

class GoRentLogoutPage(View):
	def get(self, request):
		request.session.clear()
		request.session.flush()
		return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)

		
class GoRentAboutPage(View):
	def get(self, request):
		return render(request, 'registers/landingPage.html')
		