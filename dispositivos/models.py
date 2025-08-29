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

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)

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
      
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
def __str__(self):
    return self.nombre
