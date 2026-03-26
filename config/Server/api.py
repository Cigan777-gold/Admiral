# apps/servers/api.py

import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from .models import Server

INSTALL_TOKEN = "SUPER_SECRET_123"  # потом вынесешь в settings


class RegisterServerView(APIView):
    def post(self, request):
        if request.data.get("install_token") != INSTALL_TOKEN:
            return Response({"error": "Invalid install token"}, status=403)

        name = request.data.get("name")

        api_key = secrets.token_hex(32)

        server = Server.objects.create(
            name=name,
            api_key=api_key
        )

        return Response({
            "api_key": api_key,
            "server_id": server.id
        })