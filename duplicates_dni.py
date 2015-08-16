# -*- coding: utf-8 -*-
""" encontrar numeros de DNI duplicados en diferentes padrones """
import csv

padrones = [
    {'path': 'Mendiolaza/Padron-Mendiolaza-Gobernador-2015.csv', 'dni_column': 1, 'nombre': 'Mendiolaza'}, 
    {'path': 'Villa-Allende/Padron-Villa-Allende-intendente-2015.csv', 'dni_column': 1, 'nombre': 'Villa Allende'}]


votantes = {} # DNI: los demas datos del votante y padron
dnis = [] # lista de dnis cargados
duplicados = [] # lista final de duplicados


for p in padrones:
    f = open(p['path'], 'r')
    reader = csv.reader(f)
    
    for line in reader:
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

    
# imprimir los resultados a CSV
with open('names.csv', 'w') as csvfile:
    fieldnames = ['DNI','Padron 1', 'Padron 2', 'Datos en Padron 1', 'Datos en Padron 2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for d in duplicados:
        writer.writerow({'DNI': d['dni'], 
                         'Padron 1': d['Padron1'], 
                         'Padron 2': d['Padron2'], 
                         'Datos en Padron 1': d['DatosPadron1'], 
                         'Datos en Padron 2': d['DatosPadron2']})


    