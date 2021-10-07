from database.models import *



class GoRentRegister():
	email = None
	password = None
	firstname = None
	lastName = None
	mobileNumber = None

	def emailValidator(self, email):
		self.email = email
		if RentOwner.objects.filter(email = self.email).exists()==True: #if email already exist

			return 1
	def contactNumberValidator():
		pass
	def passwordValidator():
		pass

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


