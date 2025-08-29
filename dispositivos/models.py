from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    
def __str__(self):
    return self.nombre

class Alerta(models.Model):
    id_dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    tipo_alerta = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo_alerta} - {self.descripcion[:30]}"