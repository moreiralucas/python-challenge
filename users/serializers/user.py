"""User Serializer"""

from users.models import User
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    def get_company(self, obj):
        """Return Company name"""
        return obj.company.name

    class Meta:
        model = User
        service_name = "users"
        fields = ("name","email","company")

class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        service_name = "users"
        fields = ("id", "name",)