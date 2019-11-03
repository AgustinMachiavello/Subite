from django.contrib import admin
from .models.users import *
from .models.vehiculo import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Conductor)
admin.site.register(Historial_Login)
admin.site.register(Amigo)
admin.site.register(Vehiculo)
admin.site.register(Tipo)
admin.site.register(TieneVehiculo)
admin.site.register(Ruta)
admin.site.register(Viaje)
admin.site.register(Participa_Viaje)
admin.site.register(Puntaje)
