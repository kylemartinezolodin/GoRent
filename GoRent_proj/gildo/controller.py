from database.models import *

import re

class GoRentMapSearch():
    spaces_list = Space.objects.all() 
    nearby_list = []

    @staticmethod
    def isAdressValid(address):
        return bool(re.search("^\w*\d*\.*\,*$", address))
    
    @staticmethod
    def isCoordinatesValid(coords):
        return bool(re.search("^(\d+|[0])(\.\d+)?\,(\d+|[0])(\.\d+)?$", coords)) # ONLY ALLOW X,Y OR 0.X,Y.Y FORMATS

from django.db.models.aggregates import Count
from database.models import *
from .serializers import *
import math

class GoRentNearbySpace():
	spaces_list = Space.objects.all()
	user_coord = None
	nearby_list = []

	def __init__(self, lat, long):
		self.user_coord = [lat, long]
	def distanceFormula(self, coord1, coord2):
		x1 = coord1[0]
		x2 = coord2[0]
		y1 = coord1[1]
		y2 = coord2[1]
		return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

	def getAllSpaces(self):
		self.spaces_list = Space.objects.all()
		print("boomboom")
		print(self.spaces_list)
		return(self.spaces_list)
	
	def rankSpaces(self):
		self.nearby_list.clear()
		self.getAllSpaces()
		for space in self.spaces_list:
			# space = SpaceObjectToDict(space).data # convert from python primitive object to 
			delimeterIndex = space.coordinates.find(",") #VERY URGETNT ISSUE IF comma(,) IS NOT FOUND IN THE COORDINATES IT WILL APPEND THE LAST WITH comma(,) ENTRY. U CAN FIX IT BY DESIGNATING ACTUAL LAT,LONG INFORMATION -kyle 
			print(space.coordinates)
			print("yuuuuhhh")
			latitude = float(space.coordinates[0:delimeterIndex])
			longitude = float(space.coordinates[delimeterIndex+1:])
			space_coord = [latitude,longitude]
			distance = self.distanceFormula(self.user_coord, space_coord)

			
			space_object_dict = {
				'space': space.id,
				'coordinates': space.coordinates,
				'owner': {
					'email': space.owner.email,
					'password': space.owner.password,
					'firstname': space.owner.firstname,
					'lastname': space.owner.lastname,
					'contactnumber': space.owner.contactnumber
				},
				'address': space.address,
				'price': space.price
			}
			
			print("skrrt")
			print(space)

			count = len(self.nearby_list)
			if count==0:
				print("oof")
				self.nearby_list.append({"space":space_object_dict, "distance":distance})
			else:
				print("oof2")
				i = 0
				while i != count:
					if distance < self.nearby_list[i]["distance"]:
						self.nearby_list.insert(i, {"space":space_object_dict, "distance":distance})
						break
					i = i + 1
				else:
					self.nearby_list.append({"space":space_object_dict, "distance":distance})
				# count = count - 1 
				# while count!=-1:
				# 	print(distance)
				# 	print(self.nearby_list[count]["distance"])
				# 	if distance < self.nearby_list[count]["distance"]:
				# 		print("oof3")
				# 		self.nearby_list.insert(count, {"space":space_object_dict, "distance":distance})
				# 	count = count - 1
			print("yawa")
			print(self.nearby_list)

		return self.nearby_list # returns list type

