from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Register(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=TokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.user
        refresh=serializer.validated_data['refresh']
        response_data={
            'access': str(serializer.validated_data['access']),
            'refresh': str(refresh)
        }
        return Response(response_data, status=status.HTTP_200_OK)


