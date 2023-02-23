from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class User_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.fullname
class PackageDetails(models.Model):
    pname=models.CharField(max_length=20,primary_key=True)
    amount=models.IntegerField()

class Book_Tour(models.Model):
    booking_id=models.IntegerField(primary_key=True)
    destination=models.CharField(max_length=200)
    package=models.ForeignKey(PackageDetails,on_delete=models.CASCADE)
    date=models.DateField()
    amount=models.PositiveIntegerField()

class Feedback(models.Model):
    user=models.ForeignKey(User_details,on_delete=models.CASCADE)
    suggestion=models.CharField(max_length=255)

class Payment(models.Model):
    payment_id=models.IntegerField()
    user=models.ForeignKey(User_details,on_delete=models.CASCADE)
    amount=models.CharField(max_length=25)