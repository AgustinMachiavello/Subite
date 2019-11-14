"""Tablas realacionadas al vehiculo y sus viajes"""

# Models
from django.db import models

# Date and time
from django.utils import timezone


class Vehiculo(models.Model):
    """Tabla vehiculo"""
    VehiculoId = models.AutoField(primary_key=True)
    VehiculoMatr = models.CharField(max_length=8)
    VehiculoColor = models.CharField(max_length = 20)
    TipoCod = models.ForeignKey('accounts.Tipo', on_delete = models.CASCADE, related_name='vehiculo')

class Tipo(models.Model):
    """Tabla Tipo
    
    Representa el Tipo del Vehículo"""
    TipoCod = models.AutoField(primary_key=True)
    TipoNom = models.CharField(max_length=40, unique=True)
    CapMax = models.PositiveSmallIntegerField() # MAX AND MIN

    def save(self, *args, **kwargs):
        if self.TipoNom in ['Sedán', 'Cupé', 'Hatchback', 'Descapotable', 'Roadster', 'Todoterreno',
        'Familiar', 'SUV', 'Crossover', 'Pick-Up', 'Deportivo']:
            return super(Tipo, self).save(*args, **kwargs)
        else:
            raise Exception('Tipo no válido')
            return None
        
class TieneVehiculo(models.Model):
    """Tabla Tiene Vehículo
    
    Relaciona al vehículo con su usuario"""
    CondId = models.ForeignKey('accounts.Conductor', on_delete= models.CASCADE, related_name='tiene_vehiculo_cond')
    VehiculoId = models.ForeignKey('accounts.Vehiculo', on_delete=models.CASCADE, related_name='tiene_vehiculo_veh')


class Ruta(models.Model):
    """Tabla Ruta
    
    Representa el trayecto que recorre el conductor"""
    RutaId = models.AutoField(primary_key=True)
    UsuId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='ruta_usu')
    OrigenLat = models.FloatField() # Latitud
    DestinoLat = models.FloatField()
    OrigenLon = models.FloatField() # Longitud
    DestinoLon = models.FloatField()

class Viaje(models.Model):
    """Tabla Viaje"""
    ViajeId = models.AutoField(primary_key=True)
    CondId = models.ForeignKey('accounts.Conductor', on_delete=models.CASCADE, null=False, related_name='viaje_cond')
    VehiculoId = models.ForeignKey('accounts.Vehiculo', on_delete=models.CASCADE, null=False, related_name='viaje_veh')
    ViajeFecha = models.DateTimeField()
    ViajeRuta = models.ForeignKey('accounts.Ruta', on_delete=models.CASCADE, null=False, related_name='viaje_ruta')


class Participa_Viaje(models.Model):
    """Tabla Participa Viaje"""
    UsuId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, null=False, related_name='particia_viaje_usu')
    ViajeId = models.ForeignKey('accounts.Viaje', on_delete=models.CASCADE, null=False, related_name='participa_viaje_viaje')
    HoraSubida = models.TimeField()
    OrigenLat = models.FloatField(default=0) # Latitud
    OrigenLon = models.FloatField(default=0) # Longitud
    DestinoLat = models.FloatField(default=0)
    DestinoLon = models.FloatField(default=0)

class Puntaje(models.Model):
    """Tabla Puntaje"""
    UsuId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='puntaje_usu')
    ViajeId = models.ForeignKey('accounts.Viaje', on_delete=models.CASCADE, null=False, related_name='puntaje_viaje')
    AutorId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, null=False, related_name='puntaje_autor')
    Puntaje = models.PositiveIntegerField()
    Descr = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.Puntaje >=0 and self.Puntaje <= 5:
            return super(Puntaje, self).save(*args, **kwargs)
        else:
            raise Exception('Puntaje no válido')
            return None 




