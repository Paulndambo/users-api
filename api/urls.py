from django.contrib.auth.models import User
from django.urls import path
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import UserViewSet, ProfileViewSet, ProfilesUnder

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("profiles", ProfileViewSet, basename="profiles")

urlpatterns = [
    path("", include(router.urls)),
    path("users-under/<int:referrer_id>/", ProfilesUnder.as_view(), name="users-under"),
]
