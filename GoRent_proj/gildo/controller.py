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
        return bool(re.search("^\d+(\.\d*)?\,\d+(\.\d*)?$", coords))