from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()


for i in range(len(raiz)):
	provincia=raiz[i]
	print(provincia[0].text)
	for j in range(len(provincia[1])):
		print(provincia[1][j].text)