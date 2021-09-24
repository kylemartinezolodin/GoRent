from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
from django.http import JsonResponse
import json
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
			request.session["user_type"] = "RentOwner"
			request.session["user_email"] = user_object.email
			request.session["user_password"] = user_object.password

			return redirect('gildo:main_view') # CALL THIS VIEW (ANG GET FUNCTION IEXECUTE ANI)

		else:
			
			
			# return HttpResponse("Fail \n inputs: " +username +", " +password +" Para rani debug dapat jud dili maka hibaw ang mo login unsa iya sayup")
			 return render(request, 'registers/loginOwner.html', {'popUpFlag':True})
			# return JsonResponse(errorMessage)

class GoRentLoginShareePage(View):
	def get(self, request):
		return render(request, 'registers/loginSharee.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post(self, request):

		username = request.POST.get("username")
		password = request.POST.get("password")
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
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 

	def post (self,request):

		print(request.headers)
		print(str(request) + "asdadads")

		if 'application/x-www-form-urlencoded; charset=UTF-8' in request.headers["Content-Type"]:
			request = json.loads(request.body)
			emailData = {'is_emailTaken': RentOwner.objects.filter(email=request["checkemail"]).exists()}
			emailData['error_messageEmail'] = 'A user with this email already exists.'	
			return JsonResponse(emailData)
		else:
			firstName = request.POST.get("firstName")
			lastName = request.POST.get("lastName")
			email = request.POST.get("email")
			password = request.POST.get("password")
			mobileNumber = request.POST.get("mobileNumber")
			birthdate = request.POST.get("birthdate")
			occupation = request.POST.get("occupation")

			obj = RentOwner(email = email, firstname = firstName, lastname = lastName, password = password, contactnumber = mobileNumber)
			obj.save()
			return redirect('registers:loginOwner_view')

class GoRentShareeRegisterPage(View):	
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
			shareeFirstName = request.POST.get("firstName")
			shareeLastName = request.POST.get("lastName")
			shareeEmail = request.POST.get("email")
			shareePassword = request.POST.get("password")
			shareeMobileNumber = request.POST.get("mobileNumber")
			shareeBirthdate = request.POST.get("birthdate")
			
			# shareeEmailData = {'is_shareeTaken': Sharee.objects.filter(email=shareeEmail).exists()}
			# shareeEmailData['error_shareeEmail'] = 'A user with this email already exists.'
			# if shareeEmailData['is_shareeTaken']:
			# 	return JsonResponse(shareeEmailData)
			# else:
			obj = Sharee(email = shareeEmail, firstname = shareeFirstName, lastname = shareeLastName, password = shareePassword, contactnumber = shareeMobileNumber)
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


		