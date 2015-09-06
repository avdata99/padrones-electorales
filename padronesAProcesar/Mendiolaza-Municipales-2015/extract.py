# -*- coding: utf-8 -*-
""" 
buscar la mejor convinacion de parámetros a convert 
para que tesseract sea mas efectivo 
"""

import os, subprocess, codecs
sdir = '/home/junar/andres/devs/padrones-electorales/padronesAProcesar/Mendiolaza-Municipales-2015'

pdf = '%s/ELECTORAL-MENDIOLAZA-X.pdf' % sdir
path_images = '%s/images' % sdir

try: os.mkdir(path_images)
except: pass

# extraer cada pagina a imagen (formato OBM)
print "Extrayendo imagenes del PDF"

# extraer solo la primera página que es de la que tenemos textos a validar
dest = '%s/padron' % path_images
params = ['pdfimages', '-l', '1', pdf, dest]
"""
pdfimages -l 1 /home/junar/andres/devs/padrones-electorales/padronesAProcesar/Mendiolaza-Municipales-2015/ELECTORAL-MENDIOLAZA-X.pdf /home/junar/andres/devs/padrones-electorales/padronesAProcesar/Mendiolaza-Municipales-2015/images/padron
"""
print "EXEC %s" % str(params)
subprocess.call(params)
archives = os.listdir(path_images)

# textos válidos a probar
nombres = [u'ABALLAY CASTAGNO, ANTUEL', u'ABALLAY CASTAGNO, AYELEN', u'ABALLAY, GABRIEL JORGE',
        u'ABALLAY, LEONARDO DAMIAN', u'ABALLAY, PABLO ADOLFO', u'ABALLAY, RAMON HERNAN', 
        u'ABALOS, FERNANDA INES', u'ABALOS, FERNANDO RODOLFO', u'ABATEDAGA, MYRIAM GISELLA', 
        u'ABATEDAGA, SELVA VIVIANA', u'ABATIDAGA, MARIA LORENA', u'ABAYAY, HECTOR HUGO', 
        u'ABAYAY, MARIANA', u'ABBA, CONSTANZA CAROLINA', u'ABBIATTI, HILDA MABLE', u'ABDO, MARIA NIEVES']
direcciones = [u'VALLE DEL SOL-REINA MORA 70', u'REINA MORA 70', u'VALLE DEL SOL-REINA MORA S/N', 
                u'LAS ABELIAS 369', u'EL TALAR- LAVANDA 185', u'LAS ABELIAS 359', u'LA ALAMEDA 4407', 
                u'LA ALAMEDA 4407', u'LOS CACTUS B° CENTRO 492', u'LA ALAMEDA B° EL TALAR 1280', u'LOS TALAS 182', 
                u'LA ALAMEDA B° EL TALAR 1280', u'AZARERO 242', u'LAS ABELIAS 34']
DNIS = ['36984533', '32541258', '8390126', '27529519', '24471819', '29086794', '25401107', 
        '4706433', '18176741', '20519991', '25482229', '14449264', '40522077', '29207515', 
        '1938747']

# cortar en dos y aplicar parametros variables
pbm = '%s/padron-000.pbm' % path_images
# partir cada imagen en dos columnas y aplicarle distintos parametros
params_test = {'-density': [200, 288], 
          '-threshold': ['35%', '50%', '65%'],
          '-colorspace': ['Gray'],
          '-depth': [6, 8, 10],
          '-resample': ['200x200', '150x150', '250x250']}

res = {}
for k, v in params_test.iteritems():
    for value in v:
        png_dest = '%s/padron%s%s.png' % (path_images, k, str(value))
        p = '%s %s' % (k, str(value))
        print "Converting %s" % p
        params = ['convert', pbm, '-crop', '50%x100%', '+repage', k, str(value), png_dest]
        print "EXEC %s" % str(params)
        subprocess.call(params)
        
        # se crean dos archivos (columnas), me interesa el primero
        png1 = png_dest.replace('.png', '-0.png')
        dest1 = png_dest.replace('.png', '')
        print "Tesseract %s" % p
        # for i in *png; do echo tesseract $i; tesseract $i $i -l spa; done
        params = ['tesseract', png1, dest1, '-l', 'spa']
        print "EXEC %s" % str(params)
        subprocess.call(params)
        dest1 = '%s.txt' % dest1
        # probar la pagina 1 con datos reales y conseguir asi un porcentaje de efectividad
        # y elegir la mejor convinacion de parametros a convert
        print "testing %s" % p
        f = codecs.open(dest1, 'r', encoding='utf8')
        data = f.read()
        oks = 0.0
        tot = 0.0
        for n in nombres:
            tot += 1
            if n in data: oks += 1
                
        for n in direcciones:
            tot += 1
            if n in data: oks += 1

        for n in DNIS:
            tot += 1
            if n in data: oks += 1

        final = 100.0 * oks/tot
        res[p] = final
        print "===================="
        print "FINAL %s %.2f" % (p, final)
        print "===================="

print str(res)
        
