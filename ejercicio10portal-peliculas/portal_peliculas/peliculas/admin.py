from django.contrib import admin
from .models import Pelicula, Genero, Usuario

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Usuario)