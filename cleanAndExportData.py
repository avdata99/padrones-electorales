# -*- coding: utf-8 -*-
""" Exportar a un csv unificado los datos de todos los padrones. """
import csv
import codecs
import os

# cargar todos los padrones al sistema
pi = open('padrones_index.csv', 'r')
reader = csv.reader(pi)
padrones = []

for line in reader:
    # path, dni_column, nombre, calle_column, calle_nro_column, depto_column, barrio_column, clase = line
    padron = {'path': line[0],'dni_column': int(line[1]), 'nombre': line[2],'calle_column': int(line[3]),
                'calle_nro_column': int(line[4]), 'depto_column': int(line[5]),'barrio_column': int(line[6]),
                'clase': int(line[7])}

    # detectar si hay un <cleaner>
    ps = padron['path'].split('/')
    padron['folder'] = ps[1]
    cleaner = '%s/%s/cleaner.py' % (ps[0], padron['folder'])
    if not os.path.exists(cleaner):
        print '%s NO tienen cleaner %s' % (padron['nombre'], cleaner)
        cleaner = None
    else:
        print '%s SI tienen cleaner %s' % (padron['nombre'], cleaner)

    padron['cleaner'] = cleaner
    padrones.append(padron)

row_id = 0

# Abrir archivo de datos limpios
with open('datos_limpios.csv', 'w') as csvfile:
    fieldnames = ['ID','Padron', 'DNI', 'Domicilio', 'Clase']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for p in padrones:
        f = open(p['path'], 'r')
        reader = csv.reader(f)

        for line in reader:
            # -------------------DNIs--------------------------------------------
            try:
                dni = line[p['dni_column']]
                dni = str(dni).strip()
                dni = dni.replace('.', '')
                if dni[0] == "0":
                    dni = dni[1:]
                dni = int(dni)
            except Exception, e:
                # Solo falla cuando lee el header de algunos archivos
                print "Error en DNI de Padron %s" % p['nombre']
                continue
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
                #domicilios[p['nombre']]['errores'].append(line)
                continue

            # quitar espacios multiples
            try:
                domicilio = domicilio if type(domicilio) == unicode else domicilio.decode('utf-8')
            except Exception, e:
                print "type %s" % str(type(domicilio))
                print "DOM error %s" % domicilio
                print str(e)
                exit(1)

            domicilio = ' '.join(domicilio.split())
            domicilio = domicilio.upper()

            # Testing cleaner ----
            if p['cleaner']:
                imp = 'padronesListos.%s.cleaner' % p['folder']
                _temp = __import__(imp, globals(), locals(), ['Cleaner'], -1)
                Cleaner = _temp.Cleaner
                c = Cleaner()
                domicilio = c.clean(domicilio)

            # -------------- CLASE --------------------
            if p['clase'] > -1:
                try:
                    if line[p['clase']] != "":
                        clase = int(line[p['clase']])
                        # Chancho: A muchos datos les falta el "1" en la clase
                        if clase < 1000:
                            clase = clase + 1000
                except Exception as e:
                    print "Error al castear Clase"
                    print str(line)
                    print str(e)
                    exit(1)
            else:
                # Export none para que sean Nulls al cargar DataFrames
                clase = None

            writer.writerow({'ID': row_id, 'Padron': p['nombre'], 'DNI': dni, 'Domicilio': domicilio.encode('iso-8859-1'), 'Clase': clase})
            row_id = row_id + 1
        print "Finalizado Padron: ", p['nombre']
