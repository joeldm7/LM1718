from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()

listaProvincias=['02', '04', '07']
provincias=doc.findall('provincias')
for provincia in provincias:
    if provincia.attrib['id'] in listaProvincias:
    	id = provincia.find('id')
    	print(provincia.text)