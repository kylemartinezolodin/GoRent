import math
from database.models import *

# Create your models here.
class GoRentRegisterSpace():
    space = None
    coordinates = None
    address = None
    price = None
    firstname = None
    lastname = None
    contactnumber = None

    def __init__(self, coordinates, address, price, firstname, lastname):
        self.coordinates = coordinates
        self.address = address
        self.price = price
        self.firstname = firstname
        self.lastname = lastname

    def registerSpace(self):
        obj = Space(coordinates = self.coordinates, address = self.address, price = self.price)
        obj.save()
        self.space = obj

    def addRoommates(self, firstname, lastname, contactnumber):
        roommates = SpaceRoommates(firstname, lastname, contactnumber)
        roommates.save()

    def addSpaceImage(self, path, title, caption):
        spaceimage = SpaceImage(path, title, caption)
        spaceimage.save()

	# def addRoommates #add the functions from SRS