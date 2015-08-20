# -*- coding: utf-8 -*-
""" encontrar numeros de DNI duplicados en diferentes padrones """
import csv

# cargar todos los padrones al sistema
pi = open('padrones_index.csv', 'r')
reader = csv.reader(pi)
padrones = []
for line in reader:
    # path, dni_column, nombre, calle_column, calle_nro_column, depto_column, barrio_column = line
    padron = {'path': line[0],'dni_column': int(line[1]), 'nombre': line[2],'calle_column': int(line[3]),
                'calle_nro_column': int(line[4]), 'depto_column': int(line[5]),'barrio_column': int(line[6])}
    print str(padron)
    padrones.append(padron)
             


votantes = {} # DNI: los demas datos del votante y padron
dnis = [] # lista de dnis cargados
duplicados = [] # lista final de duplicados
domicilios = {} # contador de domicilios por padron

for p in padrones:
    f = open(p['path'], 'r')
    reader = csv.reader(f)

    domicilios[p['nombre']] = {'errores': [], 'domicilios': {}} # inicializar contador de domicilios
    
    for line in reader:
        # -------------------DNIs--------------------------------------------
        dni = line[p['dni_column']]
        dni = str(dni).strip()
        dni = dni.replace('.', '')
        try:
            dni = int(dni)
        except Exception, e:
            print "DNI no valido %s %s" % (dni, str(e))
            continue

        linea = unicode(line)
        este = {'Padron': p['nombre'], 'linea': linea}
        
        if dni in dnis: # puede haber duplicados denotr de un mismo padron
            print "-----------------\nDuplicate"
            print unicode(votantes[dni])
            print unicode(este)
            duplicados.append({'dni': dni, 'Padron1': p['nombre'],
                               'Padron2': votantes[dni]['Padron'],
                               'DatosPadron1':linea,
                               'DatosPadron2':votantes[dni]['linea'],
                               })
        else:
            dnis.append(dni)
            votantes[dni] = este

        # -------------------DOMICILIOs--------------------------------------
        # algunas veces le faltan comas ...
        try:
            domicilio = line[p['calle_column']]
        except Exception, e:
            domicilios[p['nombre']]['errores'].append(line)
            print "ERROR leyendo domicilio %s (index: %d)" % (unicode(line), p['calle_column'])
            continue
            
        try:
            if p['barrio_column'] > -1:
                domicilio = '%s %s' % (line[p['barrio_column']], domicilio)
            if p['calle_nro_column'] > -1:
                domicilio = '%s %s' % (domicilio, line[p['calle_nro_column']])
            if p['depto_column'] > -1:
                domicilio = '%s %s' % (domicilio, line[p['depto_column']])
        except Exception, e:
            domicilios[p['nombre']]['errores'].append(line)
            continue
            
        # quitar espacios multiples
        domicilio = ' '.join(domicilio.split())
        domicilio = domicilio.lower()

        if domicilios[p['nombre']]['domicilios'].get(domicilio, None):
            domicilios[p['nombre']]['domicilios'][domicilio]['total'] = domicilios[p['nombre']]['domicilios'][domicilio]['total'] + 1
            domicilios[p['nombre']]['domicilios'][domicilio]['usos'].append(linea)
        else:
            domicilios[p['nombre']]['domicilios'][domicilio] = {'total': 1, 'usos': [linea]}
    
# imprimir los resultados a CSV

# DNIs repetidos
with open('dnis_repetidos.csv', 'w') as csvfile:
    fieldnames = ['DNI','Padron 1', 'Padron 2', 'Datos en Padron 1', 'Datos en Padron 2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for d in duplicados:
        writer.writerow({'DNI': d['dni'], 
                         'Padron 1': d['Padron1'], 
                         'Padron 2': d['Padron2'], 
                         'Datos en Padron 1': d['DatosPadron1'], 
                         'Datos en Padron 2': d['DatosPadron2']})


# domicilios mas usados por ciudad
for p in padrones:
    lista = domicilios[p['nombre']]['domicilios']
    lista_ord = sorted(lista.iteritems(), key=lambda d: d[1].get('total', {}), reverse=True)
    
    f = open('domicilios-mas-usados/domicilios_en_%s.txt' % p['nombre'], 'w')
    f.write('DOMICILIOS MAS USADOS EN EL PADRON: %s\n' % p['nombre'])
    f.write('Cantidad de domicilios diferentes: %d\n' % len(lista))
    f.write('Errores al leer domicilios: %d\n' % len(domicilios[p['nombre']]['errores']))
    f.write('\n===========================================\n')
    

    # primero los domicilios y su conteo
    for domicilio in lista_ord:
        k, v = domicilio
        f.write('%s :: %d USOS \n' % (k, len(v['usos'])))
        
    # ahora los dpomicilios y el detalle
    for domicilio in lista_ord:
        k, v = domicilio
        f.write('\n===========================================\n')
        f.write('%s :: %d USOS \n' % (k, len(v['usos'])))
        for usos in v['usos']:
            f.write('  - %s\n' % usos)

    # mostrar errores
    f.write('\n===========================================\n')
    f.write('ERRORES: %d\n' % len(domicilios[p['nombre']]['errores']))
        
    for error in domicilios[p['nombre']]['errores']:
        f.write('%s\n' % error)
        
    f.close()