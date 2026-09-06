from django.db import models
from django.core.exceptions import ValidationError

class OrdenTrabajo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    maquina = models.CharField(max_length=100)
    sintoma = models.TextField()
    tecnico_asignado = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, default="PENDIENTE")
    inicio_parada = models.DateTimeField(blank=True, null=True)
    fin_parada = models.DateTimeField(blank=True, null=True)

    def clean(self):
        super().clean()
        if self.inicio_parada and self.fin_parada:
            if self.fin_parada < self.inicio_parada:
                raise ValidationError("La fecha/hora de fin de parada no puede ser anterior al inicio.")

    def __str__(self):
        return f"{self.codigo} - {self.maquina}"
