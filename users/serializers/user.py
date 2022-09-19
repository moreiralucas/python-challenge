"""User Serializer"""

from rest_framework import serializers
from users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    """User Detail Serializer"""

    company = serializers.SerializerMethodField()

    def get_company(self, obj):
        """Return Company name"""
        return obj.company.name

    class Meta:
        model = User
        service_name = "users"
        fields = ("name", "email", "company")


class UserSearchSerializer(serializers.ModelSerializer):
    """User Search Serializer"""

    class Meta:
        model = User
        service_name = "users"
        fields = (
            "id",
            "name",
        )
