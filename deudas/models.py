from __future__ import unicode_literals

from django.db import models

class Deuda(models.Model):
    acreedor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    monto = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return self.acreedor

class Deudor(models.Model):
    rut = models.CharField(max_length=12)
    name = models.CharField(max_length=200)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    estadocivil = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    deuda = models.ForeignKey(Deuda)
    fecha_nac = models.DateField()

    def __str__(self):
        return self.rut