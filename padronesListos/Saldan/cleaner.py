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
            (u'ALTE ', u''),

            (u'RAMON J CARCANO', u'CARCANO'),
            (u'RAMON CARCANO', u'CARCANO'),

            (u'J MINETTI', u'MINETTI'),
            (u'JUAN MINETTI', u'MINETTI'),

            (u'SALDAN INCHIN', u'INCHIN'),
            (u'RUTA PCIAL', u'RUTA PROVINCIAL'),
            (u'J ACCASTELLI', u'ACCASTELLI'),
            (u'JOSE ACCASTELLI', u'ACCASTELLI'),
            (u'J ACASTELLI', u'ACCASTELLI'),
            (u'JOSE ACASTELLI', u'ACCASTELLI'),
            (u'ARTURO JAURETCHE', u'JAURETCHE'),
            (u'A JAURETCHE', u'JAURETCHE'),
            (u'M LEBENSOHN', u'LEBENSOHN'),
            (u'MOISES LEBENSOHN', u'LEBENSOHN'),
            (u'A MOREAU DE JUSTO', u'ALICIA MOREAU DE JUSTO'),
            (u'ALICIA M DE JUSTO', u'ALICIA MOREAU DE JUSTO'),
            (u'N AVELLANEDA', u'AVELLANEDA'),
            (u'NICOLAS AVELLANEDA', u'AVELLANEDA'),
            (u'H IRIGOYEN', u'IRIGOYEN'),
            (u'HIPOLITO IRIGOYEN', u'IRIGOYEN'),
            (u'JUSTO JOSE DE URQUIZA', u'URQUIZA'),
            (u'JUSTO J DE URQUIZA', u'URQUIZA'),
            (u'J JOSE DE URQUIZA', u'URQUIZA'),
            (u'J J DE URQUIZA', u'URQUIZA'),
            (u'O LANFRANCHI', u'LANFRANCHI'),
            (u'ORESTE LANFRANCHI', u'LANFRANCHI'),
            (u'L LUGONES', u'LUGONES'),
            (u'LEOPOLDO LUGONES', u'LUGONES'),
            (u'V SARSFIELD', u'VELEZ SARSFIELD'),
            (u'L N ALEM', u'ALEM'),
            (u'L ALEM', u'ALEM'),
            (u'LEANDRO N ALEM', u'ALEM'),
            (u'LEANDRO ALEM', u'ALEM'),
            (u'SGTO CABRAL', u'CABRAL'),
            (u'SARGENTO CABRAL', u'CABRAL'),
            (u'S JERONIMO', u'SAN JERONIMO'),
            (u'S GERONIMO', u'SAN JERONIMO'),
            (u'LISANDRO DE LA TORRE', u'DE LA TORRE'),
            (u'L DE LA TORRE', u'DE LA TORRE'),
            (u'M MORENO', u'MORENO'),
            (u'MARIANO MORENO', u'MORENO'),
            (u'ARTURO ILLIA', u'ILLIA'),
            (u'ARTURO HUMBERTO ILLIA', u'ILLIA'),
            (u'ARTURO H ILLIA', u'ILLIA'),
            (u'A ILLIA', u'ILLIA'),
            (u'V OCAMPO', u'VICTORIA OCAMPO'),
            (u'D ZIPOLI', u'ZIPOLI'),
            (u'DOMINGO ZIPOLI', u'ZIPOLI'),
            (u'CALLE ', u''),
            
            
            ))

    
    # reemplazos despues de la limpieza de barrios
    replaces2 = OrderedDict((
            (u'S/N', u''),
            (u'N°', u' '),
    ))
    
    barrios = OrderedDict((
            (u'S REMO', u''),
            
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