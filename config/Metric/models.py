# apps/monitoring/models.py

from django.db import models
from Server.models import Server

class ServerStat(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    cpu = models.FloatField(help_text="CPU(%)")
    ram = models.FloatField(help_text="RAM(%)")
    IO = models.FloatField(help_text="Input/Output(%)", null=True, blank=True)

    Cpu_Info = models.IntegerField(help_text="Total CPU Cores", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)