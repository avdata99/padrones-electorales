# -*- coding: utf-8 -*-
""" 
buscar la mejor convinacion de parámetros a convert 
para que tesseract sea mas efectivo 
"""

import os, subprocess, re, codecs
sdir = '/home/junar/andres/devs/padrones-electorales/padronesAProcesar/Mendiolaza-Municipales-2015'

pdf = '%s/ELECTORAL-MENDIOLAZA-X.pdf' % sdir
path_images = '%s/images' % sdir

try: os.mkdir(path_images)
except: pass

# extraer cada pagina a imagen (formato OBM)
print "Extrayendo imagenes del PDF"

# extraer TODAS las páginas
dest = '%s/padron' % path_images
params = ['pdfimages', pdf, dest]

print "EXEC %s" % str(params)
# YA ESTA HECHO subprocess.call(params)
archives = os.listdir(path_images)

# YA ESTA HECHO 
"""
for filename in archives:
    if not filename.endswith('.pbm'):
        continue
    pbm = '%s/%s' % (path_images, filename)
             
    png_dest = pbm + '.png'
    params = ['convert', pbm, '-crop', '50%x100%', '+repage', '-density', '200', 
                '-depth', '8', '-colorspace', 'Gray', '-threshold', '50%', '-resample', '200x200',
                '-blur', '1x1', '-sharpen', '1x1', png_dest]
    
    print "EXEC %s" % str(params)
    subprocess.call(params)
"""

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
 
f = codecs.open('results.txt', 'r', encoding='utf8')
data = f.read()
f.close()

n = 0
while data.find('\n\n') > -1:
    n += 1
    print "Reemplazo %d" % n
    data = data.replace('\n\n', '\n')

while data.find('  ') > -1:
    n += 1
    print "Reemplazo %d" % n
    data = data.replace('  ', ' ')

while data.find('\n \n') > -1:
    n += 1
    print "Reemplazo %d" % n
    data = data.replace('\n \n', '\n')

f = codecs.open('results-2.txt', 'w', encoding='utf8')
f.write(data)
f.close()