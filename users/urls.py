"""Urls for user app"""
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers
from .views import UserDetailViewSet, UserSearchViewSet, WebsiteViewset

router_api = routers.DefaultRouter()
router_api.register(r"websites", WebsiteViewset)
router_api.register(r"detail", UserDetailViewSet)
router_api.register(r"", UserSearchViewSet)

urlpatterns = [
    path("users/", include(router_api.urls)),
    path("auth/", views.obtain_auth_token),
]
