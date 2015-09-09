# -*- coding: utf-8 -*-
from django.db import models

class Elector(models.Model):
    pagina = models.IntegerField()
    columna = models.IntegerField()
    orden = models.IntegerField()
    
    nombre = models.CharField(max_length=60, null=True)
    direccion = models.CharField(max_length=60, null=True)
    dni = models.IntegerField(null=True)
    