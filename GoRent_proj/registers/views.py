from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from .models import *
	
# Create your views here.

class GoRentLoginPage(View):
	def get(self, request):
		return render(request, 'registers/login.html')


class GoRentRegisterPage(View):
	def get(self, request):
		return render(request, 'registers/renteeRegisterPage.html')
		