from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()


for provincia in raiz:
    nombre, localidades = provincia.getchildren()
    print('\nProvincia: {} {}\n  Localidades:'.format(nombre.text, provincia.attrib['id']))
    for localidad in localidades:
        print('    {} {}'.format(localidad.text, provincia.attrib['id']))