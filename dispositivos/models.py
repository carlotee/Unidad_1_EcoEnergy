from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    
def __str__(self):
    return self.nombre

class Medicion(models.Model):
    fecha_hora = models.DateTimeField()
    valor = models.FloatField()
    unidad = models.CharField(max_length=50)
    id_dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_hora} - {self.valor} {self.unidad}"