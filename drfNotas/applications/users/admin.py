from typing import Any
from django.contrib import admin
from django.forms.models import ModelForm
from django.http import HttpRequest
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "gender", "is_staff", "is_active")
    
    #fields = ("email", "full_name", "gender", "is_staff", "is_active","password","user_permissions")
    
    # buscador
    search_fields = ("email", "full_name")

    #!sobreescribimos el metodo save_model para poder encriptar la contraseña al momento de crear un usuario en djangoadmin y que este luego pueda entrar.
    def save_model(
        self, request: HttpRequest, obj: Any, form: Any, change: bool
    ) -> None:
        print(obj.gender)
        #! solo si no es un superuser y es registro de nuevo usuario (no change)
        if (not obj.is_superuser) and (not change):
            obj.set_password(obj.password)
            print(obj.password)

        return super().save_model(request, obj, form, change)

    def get_form(
        self,
        request: HttpRequest,
        obj: Any | None = None,
        change: bool = False,
        **kwargs: Any
    ) -> type[ModelForm]:
        if obj:
            obj.password = ""
        return super().get_form(request, obj, change, **kwargs)
