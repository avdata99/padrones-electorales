# -*- coding: utf-8 -*-
""" Leer el copiado y pegado """

import codecs

# columnas del CSV
# path='03-Concepcion-Con-pdfedit.txt'
path='04-pdftotext-G.txt'

f = codecs.open(path, 'r', encoding='utf8')
raw=f.read()

""" 
el archivo tiene estas propiedades (se copio y pego directo del PDF a texto, tabula no funciono)
Esta linea es la primera de alguna páginas

"""

lines = raw.split('\n')

# valores actuales que cambian cada x electores
mesa = ''

electores = [] # electores finales
imin = '' # en que estoy
to_add = {} # duplas de electores a agregar
prev_line='' # linea anterior a la actual
columnas = 2 # cantidad de columnas (siempre dos salvo al final de las mesas donde puede ser una)
cnt = 0
errores=0
for r in lines:
    cnt += 1
    if r.find('MESA NRO.:') > -1: # es la mesa
        mesa = int(r.split('MESA NRO.:')[1].strip())
        prev_line = r
        continue

    if r.find('NRO. ORDEN') > -1: # es una linea con dos electores
        # like   NRO. ORDEN ABALOS, CARINA ANDREA       NRO. ORDEN ABERCON, JORGE MIGUEL
        eles = r.split('NRO. ORDEN')
        for e in eles:
            if e.strip() == '':
                eles.remove(e)

        to_add={}
        columnas = len(eles)
        if len(eles[0].split(',')) < 2:
            print "==================\nBAD NAME %d %s\nLINE %s\nPREV %s" % (cnt, eles[0], r, prev_line)
        apellido = eles[0].split(',')[0].strip()
        nombre = eles[0].split(',')[1].strip()
        to_add['e0'] = {'nombre': nombre, 'apellido': apellido, 'mesa': mesa} 
        if columnas == 2:
            apellido = eles[1].split(',')[0].strip()
            nombre = eles[1].split(',')[1].strip()
            to_add['e1'] = {'nombre': nombre, 'apellido': apellido, 'mesa': mesa}
        imin = 'elector'
        prev_line = r
        continue

    if imin == 'elector':
        if r.strip() == '': # PERDIDO!
            errores += 1
            print "SIN DOMICILIO !!\nPREV %s" % prev_line
            to_add['e0']['domicilio'] = ''
            if columnas == 2:
                to_add['e1']['domicilio'] = ''
                
            imin=''
            
            electores.append(to_add['e0'])
            if columnas == 2:
                electores.append(to_add['e1'])

            continue
            
        imin = 'domicilio'
        partes = r.split('  ')
        partes = [x for x in partes if x.strip() != '']
                
        if len(partes) < columnas:
            print "POCOS domicilios (%d-%d) %s\nPREV %s\nPARTES: %s" % (len(partes), columnas, r, prev_line, str(partes))
            raise ValueError('POCOS domicilios')
        if len(partes) > columnas:
            print "MUCHOS domicilios %d %s\nPREV %s\nPARTES %s" % (len(partes), r, prev_line, str(partes))
            raise ValueError
        dom = partes[0].strip().replace(',', '.')
        to_add['e0']['domicilio'] = dom
        if columnas == 2:
            dom = partes[1].strip().replace(',', '.')
            to_add['e1']['domicilio'] = dom
        prev_line = r
        continue
        
    if imin == 'domicilio':
        imin = 'orden'        
        partes = r.split('  ')
        partes = [x for x in partes if x.strip() != '']
        
        try:
            to_add['e0']['orden'] = int(partes[0].strip())
            if columnas == 2:
                to_add['e1']['orden'] = int(partes[1].strip())
        except Exception, e:
            print "ORDEN Error %s\n%s\nPREV %s : %s" % (str(e), r, prev_line, str(partes))
            raise
            
        prev_line = r
        continue

    if imin == 'orden':
        # like       DOC. 22.976.882  DNI-EA 1973     DOC. 35.700.481    DNI-EA  1991 
        imin = ''
        partes = r.split(' ')
        p = [x for x in partes if x.strip() != '']

        if len(p) < (columnas*3):
            print "POCOS DATOS [%d](%d-%d) %s\nPREV %s\nPARTES: %s" % (cnt, len(p), columnas, r, prev_line, str(p))
            raise ValueError
            
        to_add['e0']['doc'] = p[0].strip()
        to_add['e0']['dni'] = int(p[1].strip().replace('.', ''))
        menos1 = False
        try: # el DNI es el tercer o cuarto param
            to_add['e0']['anio'] = int(p[2].strip())
            menos1 = True
        except:
            to_add['e0']['tipodni'] = p[2].strip()
            to_add['e0']['anio'] = int(p[3].strip())

        if columnas == 2:
            ix = 3 if menos1 else 4
            
            to_add['e1']['doc'] = p[ix].strip()
            to_add['e1']['dni'] = int(p[ix+1].strip().replace('.', ''))
            try:
                to_add['e1']['anio'] = int(p[ix+2].strip())
            except:
                to_add['e1']['tipodni'] = p[ix+2].strip()
                to_add['e1']['anio'] = int(p[ix+3].strip())

        electores.append(to_add['e0'])
        if columnas == 2:
            electores.append(to_add['e1'])

        prev_line = r
        continue
    

    

print "ELECTORES: %d" % len(electores)
print "ERRORES %d" % errores

f = codecs.open('padron.csv', 'w', encoding='utf8')
f.write('mesa,orden,DNI,tipodni,apellido,nombre,domicilio,anio\n')
for data in electores:
    mesa = data['mesa']
    orden = data.get('orden', 0)
    dni = data.get('dni', 0)
    nombre = data['nombre']
    apellido = data['apellido']
    tipodni = data.get('tipodni', 'S/D')
    anio = data.get('anio', 0)
    domicilio = data['domicilio']
    

    # f.write('{},{},{},{},{}\n'.format(orden, dni, nombre, profesion, direccion))
    f.write('%s,%s,%s,%s,%s,%s,%s,%s\n' % (mesa, orden, dni, tipodni, apellido, nombre, domicilio, anio) )

f.close()
print "END"
