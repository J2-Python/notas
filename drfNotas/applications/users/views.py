from typing import cast
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        #login
        #user=authenticate(email=email,password=password)
        #!para que no de error de pylance se hizo el cast
        user = cast(User | None, authenticate(email=email, password=password))
        if user and user.is_active:
            Token.objects.filter(user=user).delete()
            token=Token.objects.create(user=user)
            expired=timezone.now() + timedelta(minutes=30)
            user.token_expired=expired
            user.save()
            return Response({'Token': token.key},status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Credenciales no validas'},status=status.HTTP_401_UNAUTHORIZED)
        
class LoginJwtView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        #login
        #user=authenticate(email=email,password=password)
        #!para que no de error de pylance se hizo el cast
        user = cast(User | None, authenticate(email=email, password=password))
        if user and user.is_active:
            refresh=RefreshToken.for_user(user)
            return Response({
                'refres':str(refresh),
                'access':str(refresh.access_token)
            })
        else:
            return Response({'Error': 'Credenciales no validas'},status=status.HTTP_401_UNAUTHORIZED)