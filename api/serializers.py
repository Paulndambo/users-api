from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class ProfilesUnderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"