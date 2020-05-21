from django.shortcuts import redirect

def redireccion_peliculas(request):
    return redirect("/peliculas")