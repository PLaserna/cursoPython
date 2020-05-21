import string
import random
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import send_mail
from . import models
from . import views_peliculas
from portal_peliculas import settings

# Create your views here.

def registrar_usuario(request):
    return render(request, "formulario-registro-usuario.html")

def guardar_nuevo_usuario(request):
    nombre_insertado = request.POST["nombre"]
    clave_insertado = request.POST["clave"]
    email_insertado = request.POST["email"].lower().strip()
    codigo_generado = "".join(random.choices(string.ascii_letters+string.digits,k=50))
    
    res = models.Usuario.objects.filter(email = email_insertado)
    if len(res) >= 1:
        #email no disponible
        context = {
            "error_email" : "Ya hay un usuario registrado con ese Email"
            }
        return render(request, "formulario-registro-usuario.html", context)
    else:
        usuario = models.Usuario(nombre=nombre_insertado,clave=clave_insertado,email=email_insertado,codigo=codigo_generado)
        usuario.save()
        #mandamos email para validar al usuario
        asunto = "Bienvenido al portal Second Sequel"
        cuerpo_correo = """Muchas gracias por registrarte en nuestro portal.\n

        Por favor, pulsa en el siguiente enlace para validar tu correo y comenzar a registrar tus películas:\n

        http://plasdjango.pythonanywhere.com/peliculas/validar-usuario?id={}&codigo={}""".format(str(usuario.id),str(codigo_generado))
        enviado_desde = settings.EMAIL_HOST_USER
        destinatarios = [usuario.email]
        send_mail(asunto,cuerpo_correo,enviado_desde,destinatarios)

        titulo = "Registro correcto"
        mensaje = """Gracias por registrarte en nuestro portal.\n
        Hemos enviado un correo a """ + email_insertado + """ para confirmar tu cuenta de usuario."""
        context = {
            "titulo" : titulo,
            "mensaje" : mensaje
            }
        return render(request, "mensaje.html", context)

def validar_usuario(request):
    id_a_validar = request.GET["id"]
    codigo_a_validar = request.GET["codigo"]
    res = models.Usuario.objects.filter(id = id_a_validar, codigo = codigo_a_validar)

    if len(res) == 1:
        res[0].email_validado = True
        res[0].save()
        titulo = "Validación correcta"
        mensaje = "Tu cuenta ha sido validada correctamente. Ya puedes registrar tus películas"
        context = {
            "titulo" : titulo,
            "mensaje" : mensaje
            }
        return render(request, "mensaje.html", context)
    else:
        titulo = "Validación incorrecta"
        mensaje = "Los datos de validación no son correctos. Por favor contacta con el administrador del portal."
        context = {
            "titulo" : titulo,
            "mensaje" : mensaje
            }
        return render(request, "mensaje.html", context)

def login_usuario(request):
    return render(request, "login-usuario.html")
    
def identificar_usuario(request):
    email_insertado = request.POST["email"]
    clave_insertada = request.POST["clave"]
    
    res = models.Usuario.objects.filter(email = email_insertado, clave = clave_insertada)
    
    if len(res) == 0:
        context = {
            "error_login" : "Email o Contraseña incorrecta"
            }
        return render(request, "login-usuario.html", context)
    elif res[0].email_validado == False:
        context = {
            "error_login" : "Aún no ha sido validado el usuario"
            }
        return render(request, "login-usuario.html", context)
    else:
        usuario = res[0]
        request.session["id_usuario"] = usuario.id
        titulo = "Login correcto"
        mensaje = "Bienvenido " + usuario.nombre + ". Muchas gracias por identificarte. "
        context = {
            "titulo" : titulo,
            "mensaje" : mensaje
            }
        return render(request, "mensaje.html", context)
    
def logout_usuario(request):
    request.session.clear()
    #para que vuelva a listar las películas vuelvo a llamar a la función inicio
    return views_peliculas.inicio(request)
    
def mis_peliculas(request):
    usuario_actual = models.Usuario.objects.get(pk = request.session["id_usuario"])
    res = models.Pelicula.objects.order_by("-id").prefetch_related("genero","usuario").filter(usuario = usuario_actual)
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
    
    return render(request, "peliculas-usuario.html", context)
