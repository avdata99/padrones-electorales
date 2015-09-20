# -*- coding: utf-8 -*-
from collections import OrderedDict
import re


class Cleaner():

    replaces = OrderedDict((
            (u'AV ', u''),
            (u'AV. ', u''),
            (u'AVDA', u''),
            (u'AVDA.', u''),
            (u'AVENIDA', u''),
            (u'ESQ.', u'ESQ'),
            (u'ETCIA', u'ESTANCIA'),
            (u'PJE ', u''),
            
            (u'CNO LOS QUEBRACHITOS', u'QUEBRACHITOS'),  
            (u'LOS QUEBRACHITOS', u'QUEBRACHITOS'), 
            (u'CNO A LOS QUEBRACHIT', u'QUEBRACHITOS'), 
            (u'LOS QUEBRAC', u'QUEBRACHITOS'), 
            (u'CNO A L QUEBRACHITOS', u'QUEBRACHITOS'), 
            (u'CNO A QUEBRACHITOS', u'QUEBRACHITOS'),

            (u'CERRO LA CRUZ', u'CERRO DE LA CRUZ'),
            
            (u'VA AURORA R ARGENTINA', u'ARGENTINA'),
            (u'R ARGENTINA', u'ARGENTINA'),

            (u'D FUNES', u'DEAN FUNES'), 
            (u'DEAN FUENES', u'DEAN FUNES'), 
            
            (u'F AMEGHINO', u'AMEGHINO'),
            (u'FLORENTINO AMEGHINO', u'AMEGHINO'),
            (u'FLORENTINO AMEGUINO', u'AMEGHINO'), 
            (u'FLORENTIN AMEGUINO', u'AMEGHINO'), 
            (u'FLORENTINA AMEGHINO', u'AMEGHINO'),
            (u'F.AMEGHINO', u'AMEGHINO'),
             
            (u'V SARSFIELD', u'VELEZ SARSFIELD'), 
            (u'E ECHEVERRIA', u'ECHEVERRIA'),
            (u'E ECHEVARRIA', u'ECHEVERRIA'),
            (u'ESTEBAN ECHEVERRIA', u'ECHEVERRIA'),
            (u'ESTEBAN ECHEVARRIA', u'ECHEVERRIA'),
            
            (u'ALTE BROWN', u'BROWN'),
            (u'ALMIRANTE BROWN', u'BROWN'),
            (u'A BROWN', u'BROWN'),

            (u'SARGENTO CABRAL', u'CABRAL'),
            (u'SGTO CABRAL', u'CABRAL'),
            (u'S CABRAL', u'CABRAL'),

            (u'B°V°FORCHIERI-', ''),
            (u'V PORCHIERI', ''),
            
            (u'S/N', u''),
            (u'N°', u' '),
            
            ))

    
    # reemplazos despues de la limpieza de barrios
    replaces2 = OrderedDict((
            (u'L DE SAN JOSE', u''),
            (u'UNQ CENTRO', u''),
            
    ))
    
    barrios = OrderedDict((
            (u'LA LOMA ', u''),            
            (u'SAN JOSE', u''),
            
            (u'VILLA FORCHIERI', u''),
            (u'VA FORCHIERI', u''),
            (u'V FARCHIERI', u''),
            (u'FARCHIERI', u''),
            (u'V FORCHIERI', u''),
            
            (u"CIGARRALES'B'", u''),
            (u'SPILIMBERGO', u''),
            (u'CABANA', u''),
            (u'VA AURORA', u''),
            (u'V AURORA', u''),
            (u'L PROVIDENCI', u''),
            (u'LA PROVIDENCIA', u''),
            (u'GDOR PIZARRO', u''),
            (u'G PIZARRO', u''),
            (u'SAN MIGUEL', u''),
            (u'S MIGUEL', u''),
            (u'PROGRESO', u''),
            (u'VILLA TORTOSA', u''),
            (u'LAS ENSENADAS', u''),
            (u'L ENSENADAS', u''),
            (u'C DE BARRANCAS', u''),
            (u'QUEBRADA HONDA', u''),
            (u'PROGRESO', u''),
            (u'ALTO ALEGRE', u''),
            (u'CIGARRALES', u''),
            (u'TORTOSA', u''),
            (u'VA TORTOSA', u''),
            (u'PROVIDENCIA', u''),
            (u'CENTRO', u''),
            (u'RESIDENCIAL', u''),
            (u'LAS CORZUELAS', u''),
            (u'VILLA DIAZ', u''),
            (u'ENSENADAS', u''),
            (u'PQUE SERRANO', u''),
            (u'P SERRANO', u''),
            (u'PARQUE SERRANO', u''),
            (u'FONAVI', u''),
            
            ))

    def clean(self, domicilio):
        for k in self.replaces.keys():
            frm = k.upper()
            to = self.replaces[k].upper()
            domicilio = domicilio.replace(frm, to)
            if domicilio == '': 
                domicilio = 'S/D'

        domicilio = domicilio.strip()
        domicilio = ' '.join(domicilio.split()) 

        # quitar barrios
        barrios = [u'(?P<barrio>B°[\s0-9A-Z]+\-)(?P<domicilio>.*)', 
                   u'(?P<barrio>Bº[\s0-9A-Z]+\-)(?P<domicilio>.*)', 
                   u'(?P<domicilio>.*\-)(?P<barrio>B°[\s0-9A-Z]+)', 
                   u'(?P<domicilio>.*\-)(?P<barrio>Bº[\s0-9A-Z]+)', 
                   ]

        for b in barrios:
            p = re.compile(b, flags=re.UNICODE)
            m = p.search(domicilio)
            if m:
                # print m.group('barrio')
                # print m.group('domicilio')
                # print "CLEAN %s FOR %s" % (domicilio, m.group('domicilio'))
                domicilio = m.group('domicilio')
                break
        
        
        lotes = ['(?P<prev>.*)(MZ|MZA|MZNA)(?P<manzana>[\s0-9]+)(LT|L|LOTE|LTE)(?P<lote>[\s0-9]+)(?P<pos>.*)', 
                 '(?P<prev>.*)(LT|L|LOTE|LTE)(?P<lote>[\s0-9]+)(MZ|MZA|MZNA)(?P<manzana>[\s0-9]+)(?P<pos>.*)']
        for lote in lotes:
            p = re.compile(lote)
            m = p.search(domicilio)
            if m:
                manzana = m.group('manzana').strip()
                lote = m.group('lote').strip()
                prev = m.group('prev').strip()
                pos = m.group('pos').strip()
                domicilio2 = "%s MANZANA %s LOTE %s %s" % (prev, manzana, lote, pos)
                # print "Cambiando (%s) a (%s)" % (domicilio, domicilio2)
                domicilio = domicilio2
                domicilio = domicilio.strip()
                domicilio = ' '.join(domicilio.split()) 
                break

        # limpiar barrios que no entran en la regex
        for k in self.barrios.keys():
            for pref in [u'B°', u'Bº', u'B° ', u'Bº ', u'-', u'']:
                for sufix in [u'-', u'']:
                    if pref == u'' and sufix == u'': # pueden ser calles
                        continue
                    frm = '%s%s%s' % (pref, k.upper(), sufix)
                    to = self.barrios[k].upper()
                    domicilio = domicilio.replace(frm, to)
                    if domicilio == '': 
                        domicilio = 'S/D'

        # cosas despues de todo
        for k in self.replaces2.keys():
            frm = k.upper()
            to = self.replaces2[k].upper()
            domicilio = domicilio.replace(frm, to)
            if domicilio == '': 
                domicilio = 'S/D'

        domicilio = domicilio.strip()
        domicilio = ' '.join(domicilio.split()) 
        
        return domicilio