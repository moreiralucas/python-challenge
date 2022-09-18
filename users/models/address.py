"""Address model"""
from django.db import models



class Address(models.Model):
	id = models.AutoField(primary_key=True)
	zipcode = models.CharField(max_length=16)
	suite = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	street = models.CharField(max_length=128)
	localization = models.OneToOneField(
		"Localization",on_delete=models.CASCADE,
	)
