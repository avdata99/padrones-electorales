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
            (u'PJE.', u''),
            (u'ALTE ', u''),
            (u'ALTE.', u''),
            (u'SGTO ', u''),
            (u'SGTO.', u''),
            
            (u'D FUNES', u'DEAN FUNES'), 
            
            (u'F AMEGHINO', u'AMEGHINO'),
            (u'L.AMEGHINO', u'AMEGHINO'),
            
            (u'CORONA G.CLUB', u'CORONA GOLF CLUB'),
            (u'AV.CORONA GOLF CLUB', u'CORONA GOLF CLUB'),
            (u'G.C.CORONA', u'CORONA GOLF CLUB'),
            
            (u'V SARSFIELD', u'VELEZ SARSFIELD'), 
            (u'E ECHEVERRIA', u'ECHEVERRIA'),
            (u'E ECHEVARRIA', u'ECHEVERRIA'),
            (u'ESTEBAN ECHEVERRIA', u'ECHEVERRIA'),
            (u'ESTEBAN ECHEVARRIA', u'ECHEVERRIA'),
            
            (u'ALMIRANTE BROWN', u'BROWN'),
            (u'A BROWN', u'BROWN'),

            (u'SARGENTO CABRAL', u'CABRAL'),
            (u'S CABRAL', u'CABRAL'),

            (u'AV.J.D.PERON', u'PERON'),
            (u'J.D.PERON', u'PERON'),
            (u'AV.PERON', u'PERON'),
            (u'AV.PTE.PERON', u'PERON'),
            (u'AV PTE PERON', u'PERON'),
            (u'PTE PERON', u'PERON'),
            (u'PTE.PERON', u'PERON'),
            (u'J D PERON', u'PERON'),
            (u'JUAN D PERON', u'PERON'),
            (u'JUAN DOMINGO PERON', u'PERON'),
            (u'PRESIDENTE PERON', u'PERON'),
            (u'JUAN D.PERON', u'PERON'),
            
             
            (u'CAMAÑO', u'CAAMAÑO'),
            (u'AV.CAAMAÑO', u'CAAMAÑO'),
            (u'MATTHEWS CAAMAÑO', u'CAAMAÑO'),

            (u'H.YRIGOYEN', u'YRIGOYEN'),
            (u'H. YRIGOYEN', u'YRIGOYEN'),
            (u'H YRIGOYEN', u'YRIGOYEN'),
            (u'HIPOLITO YRIGOYEN', u'YRIGOYEN'),
            
            (u'SGO DEL ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'S DEL ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'S D ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'SANTIAGO D ESTERO', u'SANTIAGO DEL ESTERO'),
            
            (u'J B ALBERDI', u'ALBERDI'),
            (u'JUAN B ALBERDI', u'ALBERDI'),
            (u'J BAUTISTA ALBERDI', u'ALBERDI'),
            (u'JUAN BAUTISTA ALBERDI', u'ALBERDI'),
            
            (u'M.MARTIGNONI', u'MARTIGNONI'),
            (u'M MARTIGNONI', u'MARTIGNONI'),
            
            (u'AV.CHAMPAGNAT', u'CHAMPAGNAT'),
            (u'M.CHAMPAGNAT', u'CHAMPAGNAT'),
            (u'C.C.CHAMPAGNAT', u'CHAMPAGNAT'),
            
            (u'LA FLORIDA', u'FLORIDA'),
            
            (u'F.ROMERO', u'ROMERO'),
            (u'F. ROMERO', u'ROMERO'),
            (u'F ROMERO', u'ROMERO'),
            (u'ROMERO F.', u'ROMERO'),
            (u'ROMERO F', u'ROMERO'),
            (u'FRANCISCO ROMERO', u'ROMERO'),
            
            (u'P.DE MENDOZA', u'MENDOZA'),
            (u'PEDRO DE MENDOZA', u'MENDOZA'),
            
            (u'CARMEN PUCH', u'PUCH'),
            (u'C PUCH', u'PUCH'),
            (u'C.PUCH', u'PUCH'),
            (u'CARLOS PUCH', u'PUCH'),

            (u'R.HONDO', u'RIO HONDO'),
            (u'R HONDO', u'RIO HONDO'),
            
            (u'J.NEWBERY', u'NEWBERY'),
            (u'J NEWBERY', u'NEWBERY'),
            (u'JORGE NEWBERY', u'NEWBERY'),
            (u'12 D OCTUBRE', u'12 DE OCTUBRE'),
            
            (u'M.LASTRA', u'LASTRA'),
            (u'M LASTRA', u'LASTRA'),
            (u'MARIANO LASTRA', u'LASTRA'),
            (u'L.LUGONES', u'LUGONES'),
            (u'L LUGONES', u'LUGONES'),
            (u'LEOPOLDO LUGONES', u'LUGONES'),
            
            (u'J.HERNANDEZ', u'JOSE HERNANDEZ'),
            (u'J HERNANDEZ', u'JOSE HERNANDEZ'),
            
            (u'AV.ILLIA', u'ILLIA'),
            (u'AV. H. ILLIA', u'ILLIA'),
            (u'AV. H ILLIA', u'ILLIA'),
            (u'H.ILLIA', u'ILLIA'),
            (u'H ILLIA', u'ILLIA'),
            (u'HUMBERTO ILLIA', u'ILLIA'),

            (u'FRAGATA SARMIENTO', u'SARMIENTO'),
            (u'P.DE LEON', u'PONCE DE LEON'),
            (u'P DE LEON', u'PONCE DE LEON'),
            
            (u'M.GUEMES', u'GUEMES'),
            (u'MARTIN GUEMES', u'GUEMES'),
            (u'MARTIN DE GUEMES', u'GUEMES'),
            (u'GRAL NECOCHEA', u'NECOCHEA'),
            (u'G.C.NECOCHEA', u'NECOCHEA'),
            
            (u'AV.MITRE', u'MITRE'),
            (u'E.MITRE', u'MITRE'),
            (u'E MITRE', u'MITRE'),
            (u'EMILIO MITRE', u'MITRE'),
            (u'B.MITRE', u'MITRE'),
            (u'BARTOLOME MITRE', u'MITRE'),
            
            (u'C.RIVADAVIA', u'RIVADAVIA'),
            (u'C RIVADAVIA', u'RIVADAVIA'),
            (u'COMODORO RIVADAVIA', u'RIVADAVIA'),
            
            (u'P MORENO', u'PERITO MORENO'),
            (u'P.MORENO', u'PERITO MORENO'),
            (u'M MORENO', u'MARIANO MORENO'),
            (u'M.MORENO', u'MARIANO MORENO'),
            
            (u'PANAMERICANA KM.49', u'PANAMERICANA KM 49'),
            
            (u' KM.', u' KM '),
            (u'-KM.', u' KM '),
            (u'S/N', u''),
            (u'N°', u' '),
            
            ))

    
    # reemplazos despues de la limpieza de barrios
    replaces2 = OrderedDict((
            (u'EL ESTABLO', u''),
            
    ))
    
    barrios = OrderedDict((
            (u'LA PRADERA', u''), 
            (u'LOS PILARES', u''),
            (u'LOS SAUCES', u''),
            (u'LA LOMADA', u''),
            (u'PRIV.', u''),
            (u'CONGRESO', u''),
            (u'JAZMINES', u''),
            (u'EST.DEL PILAR', u''),
            (u'TORO', u''),
            (u'LA MASIA', u''),
            (u'SOLARES DEL NORTE', u''),
            (u'H.DEL PILAR', u''),
            (u'HARAS DEL PILAR', u''),
            (u'EL ESTABLO', u''),
            (u'LA CASUALIDAD', u''),
            (u'LA TRANQUERA', u''),
            (u'GUEMES', u''),
            
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
