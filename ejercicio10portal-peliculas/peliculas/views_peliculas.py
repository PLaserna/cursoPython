from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone
from . import models
from . import views_usuarios
import logging

# Create your views here.

def inicio(request):
    l = logging.getLogger("django.db.backends")
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())
    
    res = models.Pelicula.objects.order_by("-id").prefetch_related("genero","usuario")
    generos = models.Genero.objects.order_by("id")

    #necesario para el buscador de películas
    titulo_buscador = ""
    genero_buscador = ""
    if "genero_id" in request.GET and request.GET["genero_id"] != "":
        res = res.filter(genero = request.GET["genero_id"])
        genero_buscador = int(request.GET["genero_id"])
    if "titulo" in request.GET:
        res = res.filter(titulo__contains = request.GET["titulo"])
        titulo_buscador = request.GET["titulo"]
    
    #necesario para la paginación:
    comienzo = 0
    resultados_por_pagina = 8
    if "comienzo" in request.GET:
        comienzo = int(request.GET["comienzo"])
    total_resultados = len(res)
    res = res[comienzo:comienzo+resultados_por_pagina]
    
    anterior = comienzo - 8
    siguiente = comienzo + 8

    context = {
        "peliculas" : res,
        "generos" : generos,
        "titulo_buscador" : titulo_buscador,
        "genero_buscador" : genero_buscador,
        "anterior" : anterior,
        "siguiente" : siguiente,
        "total_resultados" : total_resultados
        }
    return render(request, "index.html", context)

def registrar_pelicula(request):
    res = models.Genero.objects.order_by("id")
    context = {
        "generos" : res
        }
    return render(request, "formulario-registro-pelicula.html", context)

def guardar_nueva_pelicula(request):
    titulo = request.POST["titulo"]
    anyo = request.POST["anyo"]
    duracion = request.POST["duracion"]
    director = request.POST["director"]
    genero_id = request.POST["genero_id"]
    formato = request.POST["formato"]
    sinopsis = request.POST["sinopsis"]
    puntuacion = request.POST["puntuacion"]
    precio = request.POST["precio"]
    ultima_modificacion = timezone.now()
    
    genero = models.Genero.objects.get(pk = genero_id)
    usuario = models.Usuario.objects.get(pk = request.session["id_usuario"])
    
    pelicula = models.Pelicula()
    pelicula.titulo = titulo
    pelicula.anyo = anyo
    pelicula.duracion = duracion
    pelicula.director = director
    pelicula.formato = formato
    pelicula.sinopsis = sinopsis
    pelicula.puntuacion = puntuacion
    pelicula.precio = precio
    pelicula.ultima_modificacion = ultima_modificacion
    
    pelicula.genero = genero
    pelicula.usuario = usuario

    pelicula.save()
    
    id_pelicula = pelicula.id
    nombre_archivo = str(id_pelicula) + ".jpg"
    
    if "poster" in request.FILES:
        f = request.FILES["poster"]
        default_storage.save(nombre_archivo, ContentFile(f.read()))
    
    titulo = "Registro correcto"
    mensaje = "Gracias por registrar tu película"
    context = {
        "titulo" : titulo,
        "mensaje" : mensaje
        }
    return render(request, "mensaje.html", context)

def borrar_pelicula(request):
    id = request.GET["id"]
    models.Pelicula.objects.get(pk = id).delete()
    nombre_archivo = str(id) + ".jpg"
    if default_storage.exists(nombre_archivo):
            default_storage.delete(nombre_archivo)

    return views_usuarios.mis_peliculas(request)

def editar_pelicula(request):
    id = request.GET["id"]
    pelicula_a_editar = models.Pelicula.objects.get(pk = id)
    context = {
        "pelicula" : pelicula_a_editar,
        "generos" : models.Genero.objects.order_by("id")
        }
    return render(request, "editar-pelicula.html", context)
    
def guardar_cambios_pelicula(request):
    pelicula = models.Pelicula.objects.get(pk = request.POST["id_pelicula"])
    pelicula.titulo = request.POST["titulo"]
    pelicula.anyo = request.POST["anyo"]
    pelicula.duracion = request.POST["duracion"]
    pelicula.director = request.POST["director"]
    pelicula.formato = request.POST["formato"]
    pelicula.sinopsis = request.POST["sinopsis"]
    pelicula.puntuacion = request.POST["puntuacion"]
    pelicula.precio = request.POST["precio"].replace(",",".")
    pelicula.ultima_modificacion = timezone.now()
    genero = models.Genero.objects.get(pk = request.POST["genero_id"])
    pelicula.genero = genero
    pelicula.save()
    
    nombre_archivo = str(pelicula.id) + ".jpg"
    
    if "poster" in request.FILES:
        if default_storage.exists(nombre_archivo):
            default_storage.delete(nombre_archivo)
        f = request.FILES["poster"]
        default_storage.save(nombre_archivo, ContentFile(f.read()))
    
    return views_usuarios.mis_peliculas(request)

def ver_ficha(request):
    id = request.GET["id"]
    pelicula_a_mostrar = models.Pelicula.objects.get(pk = id)
    context = {
        "pelicula" : pelicula_a_mostrar,
        }
    return render(request, "ficha-pelicula.html", context)