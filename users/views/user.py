"""User ViewSet"""
from typing import Optional
from django.db.models import QuerySet
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from users.serializers import UserDetailSerializer, UserSearchSerializer
from users.models import User
from users.exceptions import RequiredParamNameError


class UserDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.order_by("name")
    serializer_class = UserDetailSerializer


class UserSearchViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSearchSerializer

    def list(self, request, *args, **kwargs):
        queryset: QuerySet = User.objects.none()
        name: Optional[str] = request.query_params.get('name')

        if name is None:
            raise RequiredParamNameError()

        queryset = self.filter_queryset(self.get_queryset()).filter(name__icontains=name)

        serializer: UserSearchSerializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
