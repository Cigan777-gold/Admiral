# apps/servers/models.py

from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    MAX_CPU = models.CharField(max_length=255, null=True, blank=True)
    CPU = models.CharField(max_length=255, null=True, blank=True)
    MAX_RAM = models.CharField(max_length=255, null=True, blank=True)
    RAM = models.CharField(max_length=255, null=True, blank=True)
    MAX_GPU = models.CharField(max_length=255, null=True, blank=True)
    GPU = models.CharField(max_length=255, null=True, blank=True)
    MAX_SWAP = models.CharField(max_length=255, null=True, blank=True)
    SWAP = models.CharField(max_length=255, null=True, blank=True)
    MAX_DISK = models.CharField(max_length=255, null=True, blank=True)
    DISK = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name