# -*- coding: utf-8 -*-
""" Leer el copiado y pegado, Tabula no funciona """

import codecs

# columnas del CSV
path='Padron-1-columna.txt'

f = codecs.open(path, 'r', encoding='utf8')
raw=f.read()

lines = raw.split('\n')

paginas = [] # paginas de resultados
imin = '' # en que estoy
ix = 0 # indice del dato (recomienza para cada columna)
for r in lines:
    if r == 'APELLIDO Y NOMBRE, PROFESION, DOMICILIO, TIPO MATRICULA':
        imin = 'people'
        ix = 0 
        continue

    if r == 'MATRICULA SEXO':
        imin = 'DNIs'
        ix = 0 
        continue

    if r == "NRO":
        imin = ''
        continue
        
    if r == "ORDEN":
        imin = 'ORDEN'
        ix = 0 
        data = {} # datos duros de esta fila (aca se juntaran)
        paginas.append(data)

        continue
        
        
    if r == "40A":
        imin = ''
        continue
        
    if (r == "M" or r == "F") and imin != 'Sexo':
        imin = 'Sexo'
        ix = 0 
        continue

    if r.startswith("#20"): 
        # print "Termina página %s (%s)" % (str(r), len(paginas))
        imin = ''
        continue

    if imin == '':
        continue

        
    ix += 1
        
    if imin == 'ORDEN': # cargar el orden de los datos que hay en esta página
        data[ix] = {'order': r, 'people': 'NULL', 'Sexo': 'NULL', 'DNI': 'NULL', 
                    'nombre': 'NULL', 'profesion': 'NULL', 'direccion': 'NULL',
                    'tipodni':'NULL', 'nro': '', 'depto': ''}

    if imin == 'people':
        # malas direcciones corregidas a mano:
        # MZA 5 L 34,RUTA E 53
        # MZA 60 L 382, Q2
        # 4 HOJAS, MZA 25 LOTE 13
        partes = r.split(',')
        # puede tener 3 o 4 partes, al parecer la profesion es opcional
        if len(partes) == 3:
            nombre, direccion, tipodni = partes
            profesion = ''
        elif len(partes) == 4:
            nombre, profesion, direccion, tipodni = partes
        else:
            print "BAD INFO %s" % r 
            exit(1)
            
        data[ix]['people'] = r
        data[ix]['nombre'] = nombre
        data[ix]['profesion'] = profesion
        data[ix]['tipodni'] = tipodni
        data[ix]['depto'] = ''
        
        nro = ''
        partes = direccion.split()
        if len(partes) > 1 and partes[-1].isnumeric():
            nro = partes[-1]
            direccion = ' '.join(partes[:-1])
        data[ix]['nro'] = nro
        data[ix]['direccion'] = direccion
        # print str(data[ix])

    if imin == 'DNIs':
        data[ix]['DNI'] = r
    if imin == 'Sexo':
        data[ix]['Sexo'] = r


f = codecs.open('padron.csv', 'w', encoding='utf8')
f.write('orden,DNI,Nombre,Profesion,Calle,Nro,Depto\n')
for p in paginas:
    for ix, data in p.iteritems():
        # print str(data)
        orden = data['order']
        dni = data['DNI']
        nombre = data['nombre']
        profesion = data['profesion']
        nro = data['nro']
        depto = data['depto']
        direccion = data['direccion'] if type(data['direccion']) == str else unicode(data['direccion'])
        # f.write('{},{},{},{},{}\n'.format(orden, dni, nombre, profesion, direccion))
        f.write('%s,%s,%s,%s,%s,%s,%s\n' % (orden, dni, nombre, profesion, direccion, nro, depto) )

f.close()
print "END"
