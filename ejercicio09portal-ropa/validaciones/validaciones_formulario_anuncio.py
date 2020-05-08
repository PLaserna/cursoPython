'''
Módulo para validar mediante expresiones regulares los campos de un nuevo anuncio
@author: Pedro Laserna
'''

import re

expresion_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def validar_email(email):
    validador_email = re.compile(expresion_email)
    return validador_email.match(email)
