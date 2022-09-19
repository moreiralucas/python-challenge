"""Localization Module"""
from django.db import models


class Localization(models.Model):
    """Localization Model"""

    id = models.AutoField(primary_key=True)
    lng = models.DecimalField(max_digits=20, decimal_places=10)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
