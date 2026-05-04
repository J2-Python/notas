from django.urls import path
from .views import LoginView, LoginJwtView

app_name = "users_app"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("login-jwt/", LoginJwtView.as_view(), name="login-jwt"),
]
