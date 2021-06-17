from typing import Type
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
#from .forms import *
from database.models import *
	
# Create your views here.

class ShareeLandingPage(View):
	def get(self, request):
		rentee = RenteeRequest.objects.all()
		context = {
			'rentee' : rentee
		}
		return render(request,'sharee/sharee.html',context)
	
	def post(self, request):
		if request.method == 'POST':
			if 'btnDecline' in request.POST:
				print('delete button clicked')
				email = request.POST.get("email")
				rentee = RenteeRequest.objects.filter(email=email).delete()
				print('recorded deleted')
			return redirect('sharee:sharee_landing_view')