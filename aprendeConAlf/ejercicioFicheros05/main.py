'''
Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea 
(url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.
'''
from urllib import request

iniciales = ""

iniciales = input("Introduce las iniciales del país de la Unión Europea para consultar su PIB: ").upper()
f = request.urlopen("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
datos = f.read()
informacion = datos.decode('utf-8').split("\n")
c = 0
for linea in informacion:
    c += 1
    if c == 1 or iniciales in linea.split(",")[2]:
        print(linea)

print("\n¡Hecho!")
