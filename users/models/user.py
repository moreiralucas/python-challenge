"""User Model"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
	"""User Model"""

	username_validator = UnicodeUsernameValidator()

	EMAIL_FIELD = "email"
	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = ["email"]
	objects = UserManager()

	class Meta:
		verbose_name = _("user")
		verbose_name_plural = _("users")
		swappable = "AUTH_USER_MODEL"
		ordering = ("name",)

	id = models.AutoField(primary_key=True)
	username = models.CharField(
		max_length=128, unique=True,
		validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
	)
	email = models.CharField(max_length=128)
	website = models.CharField(max_length=128)
	phone = models.CharField(max_length=32)
	name = models.CharField(max_length=128)
	address = models.OneToOneField("Address",on_delete=models.CASCADE)
	company = models.OneToOneField("Company",on_delete=models.CASCADE)
