from django.utils import timezone
from rest_framework.authtoken.models import Token


class TokenRxpiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #!eliminar tokens expirados
        # aqui va la logica
        Token.objects.filter(user__token_expired__lt=timezone.now())
        response = self.get_response(request)
        return response
