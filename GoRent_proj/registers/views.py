from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from .models import *
	
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


class GoRentShareeRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html')

class GoRentLandingPage(View):
	def get(self, request):
		return render(request, 'registers/landingPage.html')
		