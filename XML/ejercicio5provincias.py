from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()

#Programa que lee por teclado el nombre de un municipio y muestra la provincia donde se encuentra.

provincias = doc.findall('provincia')

municipio=input("Introduzca el nombre del municipio:")

for provincia in provincias:
	nombre = provincia.find('nombre')
	localidades = provincia.findall('localidades/localidad')
	for localidad in localidades:
		if localidad.text == municipio:
			print("Esta localidad pertenece a :",nombre.text)