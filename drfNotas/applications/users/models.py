from django.db import models

# Create your models here.
## Applications/users/models.py
## Crear Applications/users/manager.py
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
class User(AbstractBaseUser,PermissionsMixin):
    #Pueder ser accesadas desde otra parte de la aplicacion
    MAS='M'
    FEM='F'
    OTROS='O'
    GENDER_CHOCES=((MAS,'Masculino'),(FEM,'Femenino'),(OTROS,'Otros'))
    email=models.EmailField(unique=True)
    full_name=models.CharField('Nombres',max_length=100)
    gender=models.CharField(max_length=1,choices=GENDER_CHOCES)
    date_birth=models.DateField('Fecha de Nacimiento',blank=True,null=True)
    # Redefiniendo campos de PermissionMixin
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    # Redefiniendo campos de AbstractBaseUser
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name']