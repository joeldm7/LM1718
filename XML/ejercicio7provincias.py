from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()
provincias=doc.findall("provincia")
buscaprovincia=str(input("Introduzca una provincia: "))


for provincia in provincias:
	nombre=provincia.find('nombre')
	localidades=provincia.findall('localidades/localidad')
	if nombre.text==buscaprovincia:
		for localidad in localidades:
			if localidad.attrib["c"]=="1":
print (localidad.text)
