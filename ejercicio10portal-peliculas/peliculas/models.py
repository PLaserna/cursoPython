from django.db import models

# Create your models here.

class Genero(models.Model):
    texto = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.texto

class Usuario(models.Model):
    nombre = models.CharField(max_length = 150)
    clave = models.CharField(max_length = 150)
    email = models.EmailField(unique = True)
    email_validado = models.BooleanField(default=False)
    codigo = models.CharField(max_length = 60, unique = True)
    
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length = 150)
    anyo = models.PositiveSmallIntegerField()
    duracion = models.CharField(max_length = 10)
    director = models.CharField(max_length = 100)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    formato = models.CharField(max_length = 100)
    sinopsis = models.TextField(max_length = 2000)
    puntuacion = models.PositiveSmallIntegerField()
    precio = models.FloatField(default = 0)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    ultima_modificacion = models.DateTimeField(verbose_name="ultima modificación")
    
    def __str__(self):
        return self.titulo + " precio: " + str(self.precio).replace(".",",")