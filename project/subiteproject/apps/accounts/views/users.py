# Django REST Framework
from rest_framework import mixins, viewsets, status

# Django REST Framework
from rest_framework import serializers
from rest_framework.permissions import AllowAny

# Models
from subiteproject.apps.accounts.models.users import Usuario, Conductor
from subiteproject.apps.accounts.models.vehiculo import Viaje, Participa_Viaje, Ruta, TieneVehiculo, Vehiculo

# Date and time
from django.utils import timezone


class UsuarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'Tel',
            'UsuFechNac',
            'password',
        ]

class ViajeModelSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return data

    def create(self, data):
        print(data)
        condId = data['ViajeRuta'].UsuId.UsuId
        conductor = Conductor.objects.get(id=condId)
        vehiculo = TieneVehiculo.objects.get(CondId=condId).VehiculoId
        viaje = Viaje.objects.create(CondId=conductor, VehiculoId=vehiculo, ViajeFecha=timezone.now(), ViajeRuta=data['ViajeRuta'])
        return viaje
    class Meta:
        model = Viaje
        fields = [
            'ViajeRuta',
        ]



class UsuariosViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """View set para usuarios
    
    Encargado de la creación, actualización y eliminación de usuarios
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioModelSerializer
    lookup_field = 'id'

    def get_permissions(self):
        print("PERMISO:", self.action)
        permissions = [AllowAny,]
        return [p() for p in permissions]


class ViajesViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """View set para viajes
    
    Encargado de la creación, actualización y eliminación de viajes
    """
    queryset = Viaje.objects.all()
    serializer_class = ViajeModelSerializer
    lookup_field = 'id'

    def get_permissions(self):
        print("PERMISO:", self.action)
        permissions = [AllowAny,]
        return [p() for p in permissions]
