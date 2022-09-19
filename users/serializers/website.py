"""Website Serializer"""

from rest_framework import serializers
from users.models import User


class WebsiteSerializer(serializers.ModelSerializer):
    """Website Serializer"""

    class Meta:
        model = User
        service_name = "websites"
        fields = ("website",)
