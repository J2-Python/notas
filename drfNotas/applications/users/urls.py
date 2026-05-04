from django.urls import path
from .views import LoginView, LoginJwtView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
app_name = "users_app"

urlpatterns = [
    #!Esta ruta ya no la vamos a usar porque ya tenemos el proceso de login
    #path("api/token", TokenObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("login-jwt/", LoginJwtView.as_view(), name="login-jwt"),
]
