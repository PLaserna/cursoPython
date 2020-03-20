'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if palabra1[-1] == palabra2[-1] and len(palabra1) > 1 and len(palabra2) > 1: 
    if len(palabra1) > 2 and len(palabra2) > 2:
        if palabra1[-3] == palabra2[-3]:
            print(palabra1 + " y " + palabra2 + " riman")
        else:
            print(palabra1 + " y " + palabra2 + " riman un poco")
    elif palabra1[-2] == palabra2[-2]:
        print(palabra1 + " y " + palabra2 + " riman un poco")
    else:
        print(palabra1 + " y " + palabra2 + " no riman")
else:
    print(palabra1 + " y " + palabra2 + " no riman")
