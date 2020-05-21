from django.urls import path
from . import views_peliculas, views_usuarios

urlpatterns = [
    path("", views_peliculas.inicio),
    path("registrar-pelicula", views_peliculas.registrar_pelicula),
    path("guardar-nueva-pelicula", views_peliculas.guardar_nueva_pelicula),
    path("registrar-usuario", views_usuarios.registrar_usuario),
    path("guardar-nuevo-usuario", views_usuarios.guardar_nuevo_usuario),
    path("login-usuario", views_usuarios.login_usuario),
    path("identificar-usuario", views_usuarios.identificar_usuario),
    path("logout-usuario", views_usuarios.logout_usuario),
    path("mis-peliculas", views_usuarios.mis_peliculas),
    path("borrar-pelicula", views_peliculas.borrar_pelicula),
    path("editar-pelicula", views_peliculas.editar_pelicula),
    path("guardar-cambios-pelicula", views_peliculas.guardar_cambios_pelicula),
    path("ficha-pelicula", views_peliculas.ver_ficha),
    path("validar-usuario", views_usuarios.validar_usuario),
    ]