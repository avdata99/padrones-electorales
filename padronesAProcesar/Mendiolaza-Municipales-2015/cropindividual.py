# -*- coding: utf-8 -*-
""" 
buscar la mejor convinacion de parámetros a convert 
para que tesseract sea mas efectivo 
"""

import os, subprocess, re # , codecs
sdir = '/home/junar/andres/devs/padrones-electorales/padronesAProcesar/Mendiolaza-Municipales-2015'

pdf = '%s/ELECTORAL-MENDIOLAZA-X.pdf' % sdir
path_pbms = '%s/323pages' % sdir

try: os.mkdir(path_pbms)
except: pass

# extraer cada pagina a imagen (formato OBM)
print "Extrayendo imagenes del PDF"

# extraer TODAS las páginas
dest = '%s/padron' % path_pbms
params = ['pdfimages', pdf, dest]
# limitar paginas params = ['pdfimages', '-l', '10', pdf, dest]
print "EXEC %s" % str(params)
# listo subprocess.call(params)

archives = os.listdir(path_pbms)

# los pares de una forma y los imapares de otra
for filename in archives:
    if not filename.endswith('.pbm'):
        continue
        
    pat = '(padron\-)(?P<page>[0-9]+)(\.pbm)'
    p = re.compile(pat)
    m = p.search(filename)
    page = int(m.group('page').strip())
    # if page > 10: continue 
    # if page < 300: continue 
    if page < 309: continue 
    if page > 313: continue 
    
    pbm = '%s/%s' % (path_pbms, filename)

    crops = []
    if page % 2 == 0: # es par
        jump_x = 812 # ancho de la columna
        jump_y = 141.5 # alto de cada fila
        jump_col2_y = 2 # en la segunda columna ir un poco mas abajo, esta levemente cruzado
        starting_x = 55
        starting_y = 390
        """ no uso el orden, es mucho 
        orden_wi = 110; orden_he = 40; orden_x = starting_x + 0; orden_y = starting_y + 45
        for x in range(16):
            crp = '%dx%d+%d+%d' % (orden_wi, orden_he, orden_x, orden_y + (x * jump_y))
            page_name = 'ord-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (orden_wi, orden_he, orden_x + jump_x, orden_y + (x * jump_y) + jump_col2_y)
            page_name = 'ord-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})
        """

        direccion_wi = 630; direccion_he = 50; direccion_x = starting_x + 140; direccion_y = starting_y + 38
        for x in range(16):
            crp = '%dx%d+%d+%d' % (direccion_wi, direccion_he, direccion_x, direccion_y + (x * jump_y))
            page_name = 'direccion-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (direccion_wi, direccion_he, direccion_x + jump_x, direccion_y + (x * jump_y) + jump_col2_y)
            page_name = 'direccion-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})


        nombre_wi = 610; nombre_he = 50; nombre_x = starting_x + 150; nombre_y = starting_y
        for x in range(16):
            crp = '%dx%d+%d+%d' % (nombre_wi, nombre_he, nombre_x, nombre_y + (x * jump_y))
            page_name = 'nombre-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (nombre_wi, nombre_he, nombre_x + jump_x, nombre_y + (x * jump_y) + jump_col2_y)
            page_name = 'nombre-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})


        dni_wi = 200; dni_he = 50; dni_x = starting_x + 195; dni_y = starting_y + 85
        for x in range(16):
            crp = '%dx%d+%d+%d' % (dni_wi, dni_he, dni_x, dni_y + (x * jump_y))
            page_name = 'dni-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (dni_wi, dni_he, dni_x + jump_x, dni_y + (x * jump_y) + jump_col2_y)
            page_name = 'dni-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})
        
        
    else:
        jump_x = 812 # ancho de la columna
        jump_y = 141.5 # alto de cada fila
        jump_col2_y = 10 # en la segunda columna ir un poco mas abajo, esta levemente cruzado
        starting_x = 100
        starting_y = 290

        """ no uso el orden, es mucho 
        orden_wi = 110; orden_he = 40; orden_x = starting_x; orden_y = starting_y + 55
        for x in range(16):
            crp = '%dx%d+%d+%d' % (orden_wi, orden_he, orden_x, orden_y + (x * jump_y))
            page_name = 'ord-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (orden_wi, orden_he, orden_x + jump_x, orden_y + (x * jump_y) + jump_col2_y)
            page_name = 'ord-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})
        """

        direccion_wi = 630; direccion_he = 50; direccion_x = starting_x + 120; direccion_y = starting_y + 38
        for x in range(16):
            crp = '%dx%d+%d+%d' % (direccion_wi, direccion_he, direccion_x, direccion_y + (x * jump_y))
            page_name = 'direccion-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (direccion_wi, direccion_he, direccion_x + jump_x, direccion_y + (x * jump_y) + jump_col2_y)
            page_name = 'direccion-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})


        nombre_wi = 610; nombre_he = 50; nombre_x = starting_x + 140; nombre_y = starting_y + 5
        for x in range(16):
            crp = '%dx%d+%d+%d' % (nombre_wi, nombre_he, nombre_x, nombre_y + (x * jump_y))
            page_name = 'nombre-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (nombre_wi, nombre_he, nombre_x + jump_x, nombre_y + (x * jump_y) + jump_col2_y)
            page_name = 'nombre-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})


        dni_wi = 200; dni_he = 50; dni_x = starting_x + 195; dni_y = starting_y + 85
        for x in range(16):
            crp = '%dx%d+%d+%d' % (dni_wi, dni_he, dni_x, dni_y + (x * jump_y))
            page_name = 'dni-%d-col1-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})

            crp = '%dx%d+%d+%d' % (dni_wi, dni_he, dni_x + jump_x, dni_y + (x * jump_y) + jump_col2_y)
            page_name = 'dni-%d-col2-page-%d.png' % (x, page)
            crops.append({'name': page_name, 'crop': crp})
        
    for c in crops:
        png_dest = '%s/%s' % (path_pbms, c['name'])
        params = ['convert', pbm, '-crop', c['crop'], '+repage', '-density', '200', 
                    '-depth', '8', '-colorspace', 'Gray', '-threshold', '50%', '-resample', '200x200',
                    '-blur', '1x1', '-sharpen', '1x1', png_dest]
    
        print "EXEC %s" % str(params)
        subprocess.call(params)

        # leer texto

        params = ['tesseract', png_dest, png_dest, '-l', 'spa']
        print "EXEC %s" % str(params)
        subprocess.call(params)
        

"""
# ver los pngs resultantes e ir grabandolo en un archivod de texto nuevo
archives = os.listdir(path_images)

subprocess.call('echo "Padron Mendiolaza municipales 2015" > results.txt', shell=True)
for filename in archives:
    if not filename.endswith('.png'):
        continue

    # detectar pagina y columna padron-293.pbm-0.png
    pat = '(padron\-)(?P<padron>[0-9]+)(\.pbm\-)(?P<columna>[0-9]+)(\.png)'
    p = re.compile(pat)
    m = p.search(filename)
    padron = m.group('padron').strip()
    columna = m.group('columna').strip()
    
    print "Tesseract %s (%s %s)" % (filename, padron, columna)
    ex = 'echo "======%s======%s" >> results.txt' % (padron, columna)
    
    subprocess.call(ex, shell=True)
    
    png = '%s/%s' % (path_images, filename)
    
    params = ['tesseract', png, png, '-l', 'spa']
    print "EXEC %s" % str(params)
    subprocess.call(params)
    dest = '%s.txt' % png

    ex = 'cat ' + dest + ' >> results.txt'
    print ex
    subprocess.call(ex, shell=True)

"""