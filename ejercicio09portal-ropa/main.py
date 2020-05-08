'''
Aplicación web para gestión de portal de anuncios sobre venta de ropa
@author: Pedro Laserna
'''

import string
import random
import os
from flask import Flask
from flask.templating import render_template
from flask.globals import request, session
from flask_mail import Mail, Message
from clases import modelo
from operaciones_bd import operaciones_bd_anuncios
from validaciones import validaciones_formulario_anuncio

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'plas.python01@gmail.com'
app.config['MAIL_PASSWORD'] = 'efvsmyyewwmroqji'
mail = Mail(app)

#lo siguiente es obligatorio para poder utlilizar la sesión
app.secret_key = "ejemplo_clave_secreta"

#ruta para la administración del portal
@app.route("/admin/")
def inicio_administracion():
    return render_template("admin/login.html", error_login = "")

#controlamos las distintas rutas para el admin
@app.route("/admin/<string:ruta>", methods=["POST","GET"])
def administracion(ruta):
    if ruta == "login-admin":
        pass_introducido = request.form["clave"]
        if pass_introducido == "1234":
            session["identificado"] = "ok"
            anuncios = operaciones_bd_anuncios.obtener_anuncios()
            return render_template("admin/listado-anuncios-admin.html", var_anuncios = anuncios)
        else:
            return render_template("admin/login.html", error_login = "Contraseña incorrecta")

    if not "identificado" in session:
        mensaje = "Te has colado, identifícate de nuevo"
        return render_template("admin/mensaje-informativo-admin.html", var_mensaje = mensaje)

    if ruta == "borrar-anuncio":
        id = request.args["id"]
        operaciones_bd_anuncios.borrar_anuncio(id)
        anuncios = operaciones_bd_anuncios.obtener_anuncios()
        try:
            #borramos la foto y si no existe no hace nada ("except")
            os.remove("static/imagenes/" + str(id) + ".jpg")
        except:
            pass
        return render_template("admin/listado-anuncios-admin.html", var_anuncios = anuncios)

    if ruta == "editar-anuncio":
        id = request.args["id"]
        prenda_a_editar = operaciones_bd_anuncios.obtener_anuncio_por_id(id)
        categorias = operaciones_bd_anuncios.obtener_categorias() 
        return render_template("admin/editar-anuncio.html", prenda = prenda_a_editar, var_categorias = categorias)

    if ruta == "guardar-cambios-anuncio":
        #obtenemos los datos del formulario
        id = request.form["id"]
        id_categoria = request.form["categoria"]
        genero = request.form["genero"]
        marca = request.form["marca"].upper()
        talla = request.form["talla"]
        precio = request.form["precio"].replace(",",".")
        email = request.form["email"]
        email_correcto = validaciones_formulario_anuncio.validar_email(email)
        if not email_correcto:
            mensaje = "El email introducido no es válido."
            return render_template("admin/mensaje-informativo-admin.html", var_mensaje = mensaje)
        descripcion = request.form["descripcion"]
        email_valido = request.form["email-valido"]
        #con los datos recogidos preparamos el objeto a mandar a la función para guardar datos en BBDD
        prenda_guardar_cambios = modelo.Prenda(id=id,id_categoria=id_categoria,genero=genero,marca=marca,talla=talla,precio=precio,email=email,descripcion=descripcion,email_valido=email_valido)
        #finalmente actualizamos la información del anuncio en la BBDD y mostramos nuevamente el listado con la info actualizada
        operaciones_bd_anuncios.guardar_cambios_anuncio(prenda_guardar_cambios)
        #si el usuario cambio la foto la pisamos con la anterior
        if "imagen" in request.files:
            imagen = request.files["imagen"]
            if imagen.filename != "":
                imagen.save("static/imagenes/" + str(id) + ".jpg")

        anuncios = operaciones_bd_anuncios.obtener_anuncios()
        return render_template("admin/listado-anuncios-admin.html", var_anuncios = anuncios)

    if ruta == "cerrar-sesion":
        session.clear()
        return render_template("admin/login.html", error_login = "")

#ruta para validar el anuncio por email
@app.route("/validar-anuncio")
def validar_anuncio():
    id = request.args.get("id")
    codigo = request.args.get("codigo")
    resultado = operaciones_bd_anuncios.comprobar_codigo_anuncio(id,codigo)
    if resultado == 0:
        mensaje = "Código o id no válidos (id: "+str(id)+"/ codigo: "+str(codigo)+")"
        return render_template("mensaje-informativo.html", var_mensaje = mensaje)
    if resultado == 1:
        operaciones_bd_anuncios.validar_email_anuncio(id)
        mensaje = "Anuncio validado <br/><a href='/'> Volver al listado de anuncios</a>"
        return render_template("mensaje-informativo.html", var_mensaje = mensaje)

@app.route("/")
def inicio():
    anuncios = operaciones_bd_anuncios.obtener_anuncios()
    return render_template("index.html", var_anuncios = anuncios)

@app.route("/index-todos")
def inicio_todos():
    anuncios_todos = operaciones_bd_anuncios.obtener_anuncios()
    return render_template("index-todos.html", var_anuncios = anuncios_todos)

@app.route("/registrar-anuncio")
def registrar_anuncio():
    categorias = operaciones_bd_anuncios.obtener_categorias() 
    return render_template("registro-anuncio.html", var_categorias = categorias)

#esta ruta es el action del form
@app.route("/guardar-nuevo-anuncio", methods=["POST"])
def guardar_anuncio():
    id_categoria = request.form["categoria"]
    genero = request.form["genero"]
    marca = request.form["marca"].upper()
    talla = request.form["talla"]
    precio = request.form["precio"].replace(",",".")
    email = request.form["email"]
    email_correcto = validaciones_formulario_anuncio.validar_email(email)
    if not email_correcto:
        mensaje = "El email introducido no es válido."
        return render_template("mensaje-informativo.html", var_mensaje = mensaje)
    descripcion = request.form["descripcion"]
    prenda = modelo.Prenda(id_categoria=id_categoria,genero=genero,marca=marca,talla=talla,precio=precio,email=email,descripcion=descripcion)
    #generamos código de comprobación para validar el anuncio
    codigo = "".join(random.choices(string.ascii_letters+string.digits,k=100))
    id_generado = operaciones_bd_anuncios.registrar_anuncio(prenda, codigo)
    if "imagen" in request.files:
        imagen = request.files["imagen"]
        if imagen.filename:
            extension_imagen = imagen.filename.split(".")[-1]
            ruta_imagen = "static/imagenes/" + str(id_generado) + "." + extension_imagen
            imagen.save(ruta_imagen)

    #enviar email
    msg = Message("Gracias por registrar tu prenda",
        sender = "plas.python01@gmail.com",
        recipients = [email]
        )
    msg.html = "Muchas gracias por registrar tu anuncio en el portal de Pedro Laserna.<br/><a href='http://plasflask.pythonanywhere.com/validar-anuncio?id={}&codigo={}'>Pincha en este enlace para validar tu anuncio</a>".format(str(id_generado),str(codigo))
    
    mail.send(msg)
    
    mensaje = "Gracias por registrar tu anuncio"
    return render_template("mensaje-informativo.html", var_mensaje = mensaje)

#No necesarias en pythonanywhere
Flask.debug = 1
app.run()
