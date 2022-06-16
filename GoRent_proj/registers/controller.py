from database.models import *
import re


class GoRentRegister():
	email = None
	password = None
	firstname = None
	lastName = None
	mobileNumber = None
	emailRegex =  "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
	passRegex = "^([^\s\t\n\r]){9,}"
	contactRegex = "^(09|\+639)\d{9}$" #"^(09|\+639)\d{9}$/"
	def emailValidator(self, user_type, email):
		self.email = email
		emailRe = re.search(self.emailRegex,email)
		print(email)
		if emailRe is None:
			return 1
		elif user_type == "RentOwner" and RentOwner.objects.filter(email = self.email).exists()==True: #if email already exist:
			return 2
		elif user_type == "Sharee" and Sharee.objects.filter(email = self.email).exists()==True: #if email already exist:
			return 2

	def contactNumberValidator(self,user_type, contactnumber):
		self.mobileNumber = contactnumber
		contactRe = re.search(self.contactRegex, contactnumber)
		if contactRe is None:
			return 4 #if the mobile number is valid
		elif user_type=="RentOwner" and RentOwner.objects.filter(contactnumber = self.mobileNumber).exists()==True: #if number exists
			return 3 # if number exist
		elif user_type=="Sharee" and Sharee.objects.filter(contactnumber = self.mobileNumber).exists()==True: #if number exists
			return 3 # if number exist

	def passwordValidator(self, password):
		self.password = password
		passRe = re.search(self.passRegex, password)
		if passRe is None:
			return 5

class GoRentLogin():
	username = None
	password = None

	
	def credentialsValidation(self, user_type, username, password):
		self.username = username
		self.password = password

		if user_type == "Sharee":
			user_object = sharee.objects.filter(email = self.username)
		elif user_type == "RentOwner":
			user_object = RentOwner.objects.filter(email = self.username)

		if (user_object.count() == 1 and user_object[0].password == password):
			return True,user_object[0]
		else:
			return False, None


