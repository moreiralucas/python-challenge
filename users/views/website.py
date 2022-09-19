"""Website ViewSet"""
from rest_framework import mixins, viewsets
from users.serializers import WebsiteSerializer
from users.models import User


class WebsiteViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Website viewset"""
    queryset = User.objects.order_by("website")
    serializer_class = WebsiteSerializer
