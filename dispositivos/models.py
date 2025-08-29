from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    
def __str__(self):
    return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

