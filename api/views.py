from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from . serializers import UserSerializer, ProfileSerializer, ProfilesUnderSerializer
from . models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfilesUnder(APIView):
    def get(self, request, format=None, **kwargs):
        profiles = Profile.objects.filter(referrer_id=kwargs['referrer_id'])
        serializer = ProfilesUnderSerializer(profiles, many=True)
        return Response(serializer.data)

