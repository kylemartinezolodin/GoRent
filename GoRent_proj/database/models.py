from django.db import models
from django.utils import timezone

class RentOwner(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    contactnumber = models.CharField(max_length = 13) # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT
    class Meta:
        db_table = "RentOwner"

    def __str__(self):
        return "[" +self.email +"] " +self.lastname +" (RentOwner)"

class Space(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(max_length = 10)
    owner = models.ForeignKey(db_column = 'owner', to = 'database.RentOwner', on_delete = models.CASCADE, null = True) # IT CAN BE NULL ESPECIALLY WHEN A SHAREE REGISTERS THE SPACE WITHOUT THE LANDLORD REGISTERED IN GoRent
    address = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = "Space"

    def __str__(self):
        return "[" +self.id +"] " +self.coordinates

class SpaceRoommates(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    space = models.ForeignKey(db_column = 'space', to = 'database.Space', on_delete = models.CASCADE, null = True)
    contactnumber = models.CharField(max_length = 13) # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT
    
    class Meta:
            db_table = "Roommates"
            
    def __str__(self):
        return 

class SpaceImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length = 100)
    space = models.ForeignKey(db_column = 'space', to = 'database.Space', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, null = True)
    caption = models.CharField(max_length = 100, null = True)

    class Meta:
        db_table = "Images"

    def __str__(self):
        return "[" +self.id +"] " +self.space.address


class Sharee(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    contactnumber = models.CharField(max_length = 13)  # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT
    space = models.ForeignKey(db_column = 'space', to = 'database.Space', on_delete = models.CASCADE, null = True)

    class Meta:
        db_table = "Sharee"

    def __str__(self):
        return "[" +self.email +"] " +self.lastname +" (Sharee)"

class RentOwnerRenteeRequest(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    contactnumber = models.CharField(max_length = 13) # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT
    rentowner = models.ForeignKey(db_column = 'rentowner', to = 'database.RentOwner', on_delete = models.CASCADE)
    requestdate = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "RentOwnerRenteeRequest"

    def __str__(self):
        return "[" +self.email +"] " +self.firstname +" (RenteeRequest -> RentOwner) " +"[" +self.RentOwner +"] "
        
class ShareeRenteeRequest(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    contactnumber = models.CharField(max_length = 13) # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT
    sharee = models.ForeignKey(db_column = 'sharee', to = 'database.Sharee', on_delete = models.CASCADE)
    requestdate = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "ShareeRenteeRequest"

    def __str__(self):
        return "[" +self.email +"] " +self.firstname +" (RenteeRequest -> Sharee) " +"[" +self.Sharee +"] "
