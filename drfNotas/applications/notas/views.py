from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, BasePermission
# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Nota
from .serializers import NotaSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
class SoloMasculino(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if (request.user.gender=="M"):
            return True
        else:
            return False
        
class ListaNotas(ListAPIView):
    serializer_class=NotaSerializer
    #queryset=Nota.objects.all()
    #permission_classes=[IsAuthenticated,SoloMasculino]
    permission_classes=[IsAuthenticated]
    #! adicional a usuario autenticado via django admin tambien va a permitir request ccon tokens
    #authentication_classes=[TokenAuthentication]
    #!la vist aahora soporta conexiones con jwt o de sessiones de usuarios autenticados en djadmin o default
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    
    def get_queryset(self):
        queryset=Nota.objects.filter(user=self.request.user)
        return queryset