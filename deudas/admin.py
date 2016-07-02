from django.contrib import admin
from deudas.models import Deuda, Deudor

class DeudaAdmin(admin.ModelAdmin):
    list_display = ('acreedor','created_at','monto','status')

class DeudorAdmin(admin.ModelAdmin):
    list_display = ('rut','name','apellido1','apellido2','estadocivil','email','deuda','fecha_nac')    

admin.site.register(Deudor, DeudorAdmin)
admin.site.register(Deuda, DeudaAdmin)