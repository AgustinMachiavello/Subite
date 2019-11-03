"""Tablas relacionadas a los usuarios"""

# Base User model
from django.contrib.auth.models import AbstractUser

# Models
from django.db import models

# Date and time
from django.utils import timezone

# Regex
from django.core.validators import RegexValidator


class Usuario(AbstractUser):
    """Tabla usuario
    
    Hereda de la talba base AbstractUser que contiene el campo contraseña, primer y segundo nombre
    """
    UsuId = models.AutoField(primary_key=True)
    email = models.EmailField('Email', null=False, blank=False, unique=True)
    Tel = models.CharField(max_length=20)
    UsuFechNac = models.DateField(default=timezone.now)
    UsuUltimoLog = models.DateTimeField(default=timezone.now)
    UsuVerificado = models.BooleanField(default=False)
    user_created_at = models.DateTimeField(default=timezone.now)
    user_updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.UsuId:
            self.UsuFechNac = timezone.now().date()
            self.UsuUltimoLog = timezone.now()
            self.user_created_at = timezone.now()
        self.user_updated_at = timezone.now()
        return super(Usuario, self).save(*args, **kwargs)


class Conductor(models.Model):
    """Tabla conductor"""
    CondId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='conductor')
    CondUrlFotLic = models.CharField(max_length=200)


class Historial_Login(models.Model):
    """Tabla Historial Login"""
    UsuId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='historial_login')
    LogFecha = models.DateField()


class Amigo(models.Model):
    """Tabla Amigo"""
    UsuId = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='amigo_usu')
    UsuIdAmigo = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='usu_amigo')
    FecIniAmistad = models.DateField()
