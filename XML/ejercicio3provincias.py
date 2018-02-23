from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()

for i in range(len(raiz)):
	provincia=raiz[i]
	print("Provincia: ",provincia[0].text)
	print("Número de municipios: ",len(provincia[1]))