from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()

provincias=doc.findall('provincia')
municipio=str(input("Introduzca una localidad: "))

for provincia in provincias:
	nombre=provincia.find('nombre')
	localidades=provincia.findall('localidades/localidad')
	for localidad in localidades:
		if localidad.text==municipio and localidad.attrib["c"]=="1":
print("Este municipio pertenece a :",nombre.text)