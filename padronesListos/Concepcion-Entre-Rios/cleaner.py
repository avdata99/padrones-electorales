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
            (u'B° ', u'B°'),
            (u'Bª ', u'B°'),
            (u'BV. ', u''),
            (u'BV ', u''),
            
            (u'DR.CLARK', u'CLARK'), 
            (u'DR. CLARK', u'CLARK'), 
            (u'DR CLARK', u'CLARK'), 

            (u'V LAS LOMAS', u'VILLA LAS LOMAS'), 
            (u'V.LAS LOMAS', u'VILLA LAS LOMAS'), 
            (u'V. LAS LOMAS', u'VILLA LAS LOMAS'), 
            (u'VA LAS LOMAS', u'VILLA LAS LOMAS'), 
            (u'VA. LAS LOMAS', u'VILLA LAS LOMAS'), 
            (u'B°VILLA LAS LOMAS', u'VILLA LAS LOMAS'), 

            (u'STA.TERESITA', u'SANTA TERESITA'), 
            (u'STA TERESITA', u'SANTA TERESITA'), 
            (u'S TERESITA', u'SANTA TERESITA'), 
            (u'S.TERESITA', u'SANTA TERESITA'), 
            (u'S. TERESITA', u'SANTA TERESITA'), 

            (u'MARTIN RUIZ MORENO', u'RUIZ MORENO'), 
            (u'R.MORENO', u'RUIZ MORENO'), 
            (u'R MORENO', u'RUIZ MORENO'), 

            (u'R.BALBIN', u'BALBIN'), 
            (u'R BALBIN', u'BALBIN'), 
            (u'R. BALBIN', u'BALBIN'), 
            (u'RICARDO BALBIN', u'BALBIN'), 
            
            
            (u'LORENZO SARTORIO', u'SARTORIO'), 
            (u'L SARTORIO', u'SARTORIO'), 
            (u'L. SARTORIO', u'SARTORIO'), 
            (u'L.SARTORIO', u'SARTORIO'), 

            (u'PABLO LORENTZ', u'LORENTZ'), 
            (u'P LORENTZ', u'LORENTZ'), 
            (u'P. LORENTZ', u'LORENTZ'), 
            (u'P.LORENTZ', u'LORENTZ'), 
            
            (u'D FUNES', u'DEAN FUNES'), 
            
            (u'F AMEGHINO', u'AMEGHINO'),
            (u'L.AMEGHINO', u'AMEGHINO'),
            
            (u'V SARSFIELD', u'VELEZ SARSFIELD'), 
            (u'V. SARSFIELD', u'VELEZ SARSFIELD'), 
            (u'V.SARSFIELD', u'VELEZ SARSFIELD'), 
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
             
            (u'H.YRIGOYEN', u'YRIGOYEN'),
            (u'H. YRIGOYEN', u'YRIGOYEN'),
            (u'H YRIGOYEN', u'YRIGOYEN'),
            (u'HIPOLITO YRIGOYEN', u'YRIGOYEN'),
            (u'BV. HIPOLITO IRIGOYEN', u'YRIGOYEN'),
            (u'BV.HIPOLITO IRIGOYEN', u'YRIGOYEN'),
            
            
            (u'SGO DEL ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'S DEL ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'S D ESTERO', u'SANTIAGO DEL ESTERO'),
            (u'SANTIAGO D ESTERO', u'SANTIAGO DEL ESTERO'),
            
            (u'J B ALBERDI', u'ALBERDI'),
            (u'JUAN B ALBERDI', u'ALBERDI'),
            (u'J BAUTISTA ALBERDI', u'ALBERDI'),
            (u'JUAN BAUTISTA ALBERDI', u'ALBERDI'),
            
            (u'J.NEWBERY', u'NEWBERY'),
            (u'J NEWBERY', u'NEWBERY'),
            (u'JORGE NEWBERY', u'NEWBERY'),
            (u'12 D OCTUBRE', u'12 DE OCTUBRE'),
            (u'12 D.OCTUBRE', u'12 DE OCTUBRE'),
            
            (u'J.J.MILLAN', u'MILLAN'),
            (u'J.J. MILLAN', u'MILLAN'),
            (u'J J MILLAN', u'MILLAN'),
            (u'MILLAN J J', u'MILLAN'),

            (u'A ARTUSI', u'ARTUSI'),
            (u'A. ARTUSI', u'ARTUSI'),
            (u'A.ARTUSI', u'ARTUSI'),
            
            (u'MANUEL BELGRANO', u'BELGRANO'),
            (u'M.BELGRANO', u'BELGRANO'),
            (u'M BELGRANO', u'BELGRANO'),
            (u'M. BELGRANO', u'BELGRANO'),

            (u'BALBIN R', u'BALBIN'),
            (u'R BALBIN', u'BALBIN'),
            (u'R.BALBIN', u'BALBIN'),
            (u'R. BALBIN', u'BALBIN'),
            (u'RICARDO BALBIN', u'BALBIN'),
            
            (u'ALBERTO CAROSSINI', u'CAROSSINI'),
            (u'A CAROSSINI', u'CAROSSINI'),
            (u'A. CAROSSINI', u'CAROSSINI'),
            (u'A.CAROSSINI', u'CAROSSINI'),
            
            (u'ING.HENRY', u'HENRY'),
            (u'ING. HENRY', u'HENRY'),
            (u'I. HENRY', u'HENRY'),
            (u'I.HENRY', u'HENRY'),
            (u'ING HENRY', u'HENRY'),
            (u'INGENIERO HENRY', u'HENRY'),
            (u'HENRY ING', u'HENRY'),
            
            (u'ERENO', u'EREÑO'),
            
            (u'L.LOPEZ', u'LUCILO LOPEZ'),
            (u'L. LOPEZ', u'LUCILO LOPEZ'),
            (u'L LOPEZ', u'LUCILO LOPEZ'),
            (u'LUCILO B LOPEZ', u'LUCILO LOPEZ'),
            (u'L.B.LOPEZ', u'LUCILO LOPEZ'),
            (u'LOPEZ LUCILO', u'LUCILO LOPEZ'),
            
            (u'M. LOPEZ', u'MARIANO LOPEZ'),
            (u'M.LOPEZ', u'MARIANO LOPEZ'),
            (u'M LOPEZ', u'MARIANO LOPEZ'),

            (u'B.COOK', u'COOK'),
            (u'BENITO COOK', u'COOK'),
            (u'DR.B.COOK', u'COOK'),
            (u'DR BENITO COOK', u'COOK'),
            (u'DR. BENITO COOK', u'COOK'),
            (u'DR.BENITO COOK', u'COOK'),
            (u'DR. COOK', u'COOK'),
            (u'DR.COOK', u'COOK'),
            (u'DR COOK', u'COOK'),
            
            (u'COMB.DE MALVINAS', u'COMBATIENTES DE MALVINAS'),
            (u'C.DE MALVINAS', u'COMBATIENTES DE MALVINAS'),
            (u'C DE MALVINAS', u'COMBATIENTES DE MALVINAS'),
            (u'COMBAT MALVINAS', u'COMBATIENTES DE MALVINAS'),
            
            
            (u'LEANDRO ALEM', u'ALEM'),
            (u'LEANDRO N ALEM', u'ALEM'),
            (u'L N ALEM', u'ALEM'),
            (u'L.N.ALEM', u'ALEM'),
            (u'L.N. ALEM', u'ALEM'),
            (u'L ALEM', u'ALEM'),
            (u'L. ALEM', u'ALEM'),
            (u'L.ALEM', u'ALEM'),
            
            
            
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

            (u'M.GUEMES', u'GUEMES'),
            (u'MARTIN GUEMES', u'GUEMES'),
            (u'MARTIN DE GUEMES', u'GUEMES'),
            (u'GRAL NECOCHEA', u'NECOCHEA'),
            (u'G.C.NECOCHEA', u'NECOCHEA'),
            
            (u'AV.MITRE', u'MITRE'),
            (u'B.MITRE', u'MITRE'),
            (u'BARTOLOME MITRE', u'MITRE'),
            (u'BME.MITRE', u'MITRE'),

            (u'M.REIBEL', u'REIBEL'),
            (u'M. REIBEL', u'REIBEL'),
            (u'M REIBEL', u'REIBEL'),
            (u'MARTIN REIBEL', u'REIBEL'),

            (u'ALFONSINA STORNI', u'STORNI'),
            (u'A STORNI', u'STORNI'),
            (u'A.STORNI', u'STORNI'),
            (u'A. STORNI', u'STORNI'),
            (u'CVA.STORNI', u'STORNI'),
            
            (u'COL PERFECCION', u'COLONIA PERFECCION'),
            (u'COL. PERFECCION', u'COLONIA PERFECCION'),
            (u'COL.PERFECCION', u'COLONIA PERFECCION'),
            (u'CNIA.PERFECCION', u'COLONIA PERFECCION'),
            (u'CNIA PERFECCION', u'COLONIA PERFECCION'),
            (u'CNIA PERFECCION', u'COLONIA PERFECCION'),
            (u'C.PERFECCION', u'COLONIA PERFECCION'),
            (u'C. PERFECCION', u'COLONIA PERFECCION'),
            (u'C PERFECCION', u'COLONIA PERFECCION'),
            
            (u'C.RIVADAVIA', u'RIVADAVIA'),
            (u'C RIVADAVIA', u'RIVADAVIA'),
            (u'COMODORO RIVADAVIA', u'RIVADAVIA'),
            
            (u'P MORENO', u'PERITO MORENO'),
            (u'P.MORENO', u'PERITO MORENO'),
            (u'M MORENO', u'MARIANO MORENO'),
            (u'M.MORENO', u'MARIANO MORENO'),

            (u'B°HIPODROMO', u'BARRIO HIPODROMO'),
            (u'HIPODROMO', u'BARRIO HIPODROMO'),
            (u'B.HIPODROMO', u'BARRIO HIPODROMO'),
            (u'BO HIPODROMO', u'BARRIO HIPODROMO'),
            (u'BO HIPODROMO', u'BARRIO HIPODROMO'),
            
            
            
            
            (u'S/N', u''),
            (u'S/N°', u''),
            (u'N°', u' '),
            
            ))

    
    # reemplazos despues de la limpieza de barrios
    replaces2 = OrderedDict((
            
    ))
    
    barrios = OrderedDict((
            
            
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
