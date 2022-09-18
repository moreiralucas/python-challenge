"""Company model"""
from django.db import models

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	bs = models.CharField(max_length=128)
	catchphrase = models.CharField(max_length=128)
