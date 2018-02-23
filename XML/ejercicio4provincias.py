from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()


# Lee por teclado el nombre de una provincia y te muestra la provincia donde se encuentra (ejercicio4)
provincias=doc.findall("provincia")
prov_nombre=input("Introduce el nombre de la provincia: ")
for provincia in provincias:
	nombre = provincia.find('nombre')
	if nombre.text == prov_nombre:
		localidades = provincia.findall('localidades/localidad')
		for localidad in localidades:
			print (localidad.text)