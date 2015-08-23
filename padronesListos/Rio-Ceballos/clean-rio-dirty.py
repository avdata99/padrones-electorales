# -*- coding: utf-8 -*-
"""Me llega un XLSX que paso a CSV para posprocesar porque vienen los campos 
 DNI+Tipo mezclados asi como Apellido+nombre+Domicilio
 """
import csv
path = 'Rio-Ceballos-dirty.csv' # archivo con columnas mezcladas

pi = open(path, 'r')
reader = csv.reader(pi)
votantes = []
for line in reader:
    sid, orden, fulldni, persona, voto, obs = line
    if orden == '---': # saltos de página
        continue
        
    try:
        dni = fulldni.split()[0]
    except Exception, e:
        print "DNI error %s" % str(e)
        print fulldni
        exit(1)

    p = persona.split(',')
    if len(p) == 3:
        apellido, nombre, domicilio = p
    elif len(p) == 4:
        apellido, nombre, d, domicilio = p
        domicilio = '%s %s' % (d, domicilio)
    else:
        print "Persona error"
        print persona
        exit(1)

    votantes.append({'dni': dni, 'apellido': apellido, 'nombre': nombre, 'domicilio': domicilio, 'id': sid, 'orden': orden})
    print "%s - %s - %s - %s" % (dni, apellido, nombre, domicilio)

# escribir algo que me sirva mas
with open('Rio-Ceballos.csv', 'w') as csvfile:
    fieldnames = ['id', 'orden', 'dni','apellido', 'nombre', 'domicilio']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for votante in votantes:
        writer.writerow(votante)
