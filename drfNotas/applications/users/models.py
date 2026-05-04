from django.db import models
from .manager import UserManager

# Create your models here.
## Applications/users/models.py
## Crear Applications/users/manager.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    # Pueder ser accesadas desde otra parte de la aplicacion
    MAS = "M"
    FEM = "F"
    OTROS = "O"
    GENDER_CHOCES = ((MAS, "Masculino"), (FEM, "Femenino"), (OTROS, "Otros"))
    email = models.EmailField(unique=True)
    full_name = models.CharField("Nombres", max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOCES)
    date_birth = models.DateField("Fecha de Nacimiento", blank=True, null=True)
    # Redefiniendo campos de PermissionMixin
    is_staff = models.BooleanField(default=False)
    token_expired = models.DateTimeField('Token Expired', blank=True,null=True)
    is_active = models.BooleanField(default=False)
    # configuramos el manager
    #! centraliza la creación de usuarios en un solo lugar
    #! asegura que la contraseña se guarde cifrada con set_password(...)
    #! define la diferencia entre un usuario normal y un superusuario
    #! le da a Django los métodos que espera cuando usas createsuperuser
    objects = UserManager()
    # Redefiniendo campos de AbstractBaseUser
    # para ingresar a djangoadmin ahora ya usamos el email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def get_full_name(self):
        return self.full_name
