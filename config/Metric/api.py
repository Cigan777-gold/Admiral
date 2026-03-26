# apps/Metric/api.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import ServerStat
from rest_framework.serializers import ModelSerializer

from Server.models import Server
from .models import ServerStat


def get_server_from_request(request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    try:
        prefix, api_key = auth_header.split()
    except:
        return None

    if prefix != "Api-Key":
        return None

    try:
        return Server.objects.get(api_key=api_key)
    except Server.DoesNotExist:
        return None


class ReceiveStatsView(APIView):
    def post(self, request):
        server = get_server_from_request(request)

        if not server:
            return Response({"error": "Unauthorized"}, status=403)

        ServerStat.objects.create(
            server=server,
            cpu=request.data.get("cpu"),
            ram=request.data.get("ram"),
            IO=request.data.get("IO"),
        )

        return Response({"status": "ok"})
    
class ServerStatSerializer(ModelSerializer):
    class Meta:
        model = ServerStat
        fields = "__all__"


class ServerStatListView(ListAPIView):
    queryset = ServerStat.objects.all().order_by("-created_at")
    serializer_class = ServerStatSerializer