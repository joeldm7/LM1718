from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()


#print(len(raiz))

#Lista todas las Provincias con sus Municipios (Ejercicio 1 y 2)
"""for i in range(len(raiz)):
	provincia=raiz[i]
	print(provincia[0].text)
	for j in range(len(provincia[1])):
		print(provincia[1][j].text)"""

#Lista Provincias y el total de municipios que tiene cada una (ejercicio3)
"""for i in range(len(raiz)):
	provincia=raiz[i]
	print("Provincia: ",provincia[0].text)
	print("Número de municipios: ",len(provincia[1]))"""

# Lee por teclado el nombre de una provincia y te muestra la provincia donde se encuentra (ejercicio4)
provincias=doc.findall("provincia")
prov_nombre=input("Introduce el nombre de la provincia: ")
for i in provincia:
	if prov_nombre.text == provincia:
		localidades = provincia.findall('localidades/localidad')
		for localidad in localidades:
			print (localidad.text)
			break


