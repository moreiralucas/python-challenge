"""User Model"""
from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key=True)
	website = models.CharField(max_length=128)
	phone = models.CharField(max_length=32)
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	address = models.OneToOneField("Address",on_delete=models.CASCADE)
	company = models.OneToOneField("Company",on_delete=models.CASCADE)
