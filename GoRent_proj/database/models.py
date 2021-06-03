from django.db import models

class RentOwner(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    birthday = models.DateField()
    contactnumber = models.CharField(max_length = 13) # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT

    class Meta:
        db_table = "RentOwner"

    def __str__(self):
        return "[" +self.email +"] " +self.lastname +" (RentOwner)"

class Space(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(max_length = 10)
    owner = models.ForeignKey(db_column = 'owner', to = 'database.RentOwner', on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length = 100)
    price = models.DecimalField(null = True, max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = "Spaces"

    def __str__(self):
        return "[" +self.id +"] " +self.coordinates


class SpaceImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length = 100)
    space = models.ForeignKey(db_column = 'space', to = 'database.Space', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 100)

    class Meta:
        db_table = "Images"

    def __str__(self):
        return "[" +self.id +"] " +self.space.address


class Sharee(models.Model):
    email = models.EmailField(primary_key=True, max_length=254)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    birthday = models.DateField()
    contactnumber = models.CharField(max_length = 13)  # INPUT SHOULD ONLY BE IN +639 or 09 FORMAT

    class Meta:
        db_table = "Sharee"

    def __str__(self):
        return "[" +self.email +"] " +self.lastname +" (Sharee)"


