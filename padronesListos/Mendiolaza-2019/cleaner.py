# -*- coding: utf-8 -*-
""" cleaner para domicilios"""
from collections import OrderedDict
import re


class Cleaner():

    replaces = OrderedDict((
                (u'MANZANA', u'MZ'), 
                (u'MZA ', u'MZ '), 
                (u' LT ', ' LOTE'),
                (u'AV.', 'AV'),
                (u'AVDA', 'AV'),
                (u'AVENIDA', 'AV'),
                (u'ETCIA', u'ESTANCIA'),
                
                (u'ESQ.', u'ESQ'),
                (u'(DIECISEIS)', u''),
                (u'ESQUINA', u'ESQ'),
                (u'(SEIS)', u''),
                (u'(OCHO)', u''),
                (u'(NUEVE)', u''),
                
                
                (u'CUATRO', u'4'),
                (u'DIECISEIS', u'16'),
                (u'SEIS', u'6'),
                (u'SIETE', u'7'),
                (u'OCHO', u'8'),
                (u'NUEVE', u'9'),
                (u'DIEZ', u'10'),
                (u'TRECE', u'13'),
                
                (u'CALLE ', u''),
        
        
                (u'B°GOLF-', u''), 
                (u'-MENDIOLAZA GOLF-', u''), 
                (u'B°MEND GOLF-', u''), 
                (u'B°M GOLF-', u''), 
                (u'B°GOLF', u''),
                (u'B° GOLF', u''),
                (u'B°MEND.GOLF', u''),
                (u'B°MENDIOLAZA GOLF', u''),
                (u'B°MENDIOLZA GOLF', u''),
                (u'B° MEND GOLF', u''),
                (u'MENDIOLAZA GOLF', u''),
                
                (u'B°CIGARRALES A-', u''), 
                (u'B°CIGARRALES B-', u''), 
                (u'B°CIGARRALES C-', u''), 
                (u'B° CIGARRALES A-', u''), 
                (u'B° CIGARRALES B-', u''), 
                (u'B° CIGARRALES C-', u''), 
                (u'B°CAGARRALES-', u''),
                (u'B°CIGARRALES-', u''), 
                (u'B°CIGARRALES', u''), 
                (u'B°L CIGARRALES-', u''), 
                (u'B°CIG. A', u''),
                (u'B°CIG. B', u''),
                (u'B°CIG. C', u''),
                (u'B°CIG. ', u''),
                (u'B°CIG A', u''),
                (u'B°CIG B', u''),
                (u'B°CIG C', u''),
                (u'B°CIG ', u''),
                (u'-CIGARRALES-', u''),
                (u'B°LOS CIGARRALES - ', u''),
                (u'B°LOS CIGARRALES -', u''),
                (u'B°LOS CIGARRALES-', u''),
                (u'B°LOS CIGARRALES', u''),
                (u'B° LOS CIGARRALES A', u''),
                (u'B° LOS CIGARRALES B', u''),
                (u'B° LOS CIGARRALES C', u''),
                (u'B° LOS CIGARRALES', u''),
                (u'KM16', u''),
                (u'B LOS CIGARRALES A', u''),
                (u'B LOS CIGARRALES B', u''),
                (u'B LOS CIGARRALES C', u''),
                (u'B LOS CIGARRALES', u''),
                (u'(LOS CIGARRALES A)', u''),
                (u'(LOS CIGARRALES B)', u''),
                (u'(LOS CIGARRALES C)', u''),
                (u'(LOS CIGARRALES)', u''),
                (u'LOS CIGARRALES A', u''),
                (u'LOS CIGARRALES B', u''),
                (u'LOS CIGARRALES C', u''),
                (u'LOS CIGARRALES \'A\'', u''),
                (u'LOS CIGARRALES \'B\'', u''),
                (u'LOS CIGARRALES \'C\'', u''),
                (u'LOS CIGARRALES', u''),
                (u'CIGARRALES A', u''), 
                (u'- CIGARRALES', u''),
                (u'L CIGARRALES', u''),
                (u'CIGARRALES', u''),
                
                
                (u'B°L GIRAS', u''),
                (u'B°LOMAS-', u''), 
                (u'L DE MENDIOLAZA', u''),
                (u'LOMAS DE MENDIOLAZA', u''),
                
                (u'B°LOS ESPAÑOLES', ''),
                (u'-MENDIOLAZA-', u''),
                
                (u'EL TALAR - ', u''),
                (u'EL TALAR -', u''),
                (u'B°EL TALAR-', u''), 
                (u'B°TALAR-', u''), 
                (u'B° EL TALAR', u''),
                (u'EL TALAR- ', u''), 
                (u'EL TALAR ', u''), 
                (u'-TALAR-', u''),
                (u'-EL TALAR', u''),
                (u'B° TALAR', u''),
                (u'TALAR-', u''),

                (u'B° Q2-', u''), 
                (u'B Q2-', u''), 
                (u'B° Q2 -', u''), 
                (u'B Q2 -', u''), 
                (u'BARRIO Q2-', u''),
                (u'B°Q2', 'Q2'),
                (u'Q 2', 'Q2'),
                (u'-ECIA.Q2', u''),
                (u'E Q2', u'Q2'),
                (u'ECIA Q2', u'Q2'),
                (u'ESTANCIA Q2', u'Q2'),
                (u'EST Q2', u'Q2'),
                (u'EST.Q2', u'Q2'),
                (u'ESTANC Q2', u'Q2'),
                
                (u'B°V DEL SOL-', u''), 
                (u'B°VALLE DEL SOL-', u''), 
                (u'B°V D SOL', u''),
                (u'B° V D SOL', u''),
                (u'-V SOL-', u''),
                (u'B° VALLE DEL SOL', u''),
                (u'V°DEL SOL-', u''),
                (u'V°DEL SOL', u''),
                (u'VALLE DEL SOL - ', u''),
                (u'VALLE DEL SOL- ', u''),
                (u'VALLE DEL SOL-', u''),
                (u'VALLE DEL SOL', u''),
                (u'VLLE DEL SOL-', u''),
                (u'B° V.DEL SOL', u''),
                (u'V.DEL SOL', u''),
                (u'VALLE D SOL', u''),
                (u'VA DE SOL', u''),
                (u'VA DEL SOL', u''),
                (u'B° V DEL SOL', u''),
                (u'V DEL SOL', u''),
                (u'B° V D SOL', u''),
                (u'V D SOL', u''),
                (u'B° V DE SOL', u''),
                (u'V DE SOL', u''),
                
                (u'B°4 HOJAS-', u'4 HOJAS - '), 
                (u'B°4HOJAS-', u'4 HOJAS - '), 
                (u'CUATRO HOJAS ', u'4 HOJAS - '), 
                (u'B°4 HOJAS ', u'4 HOJAS - '),
                (u'4 HOLAS ', u'4 HOJAS - '),
                
                (u'B°CENTRO', u''), 
                (u'B° CENTRO', u''),
                (u'B°CENTRO ', u''),
                (u'B°CENTO-', u''),
                (u'B°CENTO', u''),
                (u'B°M CENTRO', u''),
                (u'B°MEND CENTRO', u''),
                (u'B°RES CENTRO', u''),

                (u'B°EL PERCHEL-', u''),
                (u'B°EL PERCHEL', u''),
                (u'B°PERCHEL', u''),
                (u'B° PERCHEL', u''),
                (u'B° EL PERCHEL', u''),
                (u'EL PERCHEL', u''),
                
                
                (u'BELTEVEO', u'BENTEVEO'),
                (u'BOBADILLAS', u'BOBADILLA'),
                (u'G BOBADILLA', u'GREGORIO BOBADILLA'),
                (u'GREGORIO BOBADILLA', u'BOBADILLA'),
                (u'BV. ITALIA', u'BV ITALIA'),
                (u'BVARD ITALIA/CORDOBA', u'BV ITALIA ESQ CORDOBA'),
                (u'BS AS', u'BUENOS AIRES'),
                (u'BS.AIRES', u'BUENOS AIRES'),
                (u'L HALCONES', u'LOS HALCONES'),
                (u'AV PTE ILLIA', u'ILLIA'),
                (u'BV ILLIA', u'ILLIA'),
                (u'AV T TISSERA', u'TISSERA'),
                (u'TISERA', u'TISSERA'),
                (u'TIOSSERA', u'TISSERA'),
                (u'TIBURCIO TISSERA', u'TISSERA'),
                (u'TIBORCIO TSSERA', u'TISSERA'),
                (u'T TISSERA', u'TISSERA'),
                (u'T.TISSERA', u'TISSERA'),
                
                (u'SAN JOSE DE CLASANZ', u'JOSE DE CALASANZ'),
                (u'SAN JOSE DE CALASANZ', u'JOSE DE CALASANZ'),
                (u'SAN J DE CALAZANZ', u'JOSE DE CALASANZ'),
                (u'SAN J DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'SAN J CALAZANS', u'JOSE DE CALASANZ'),
                (u'SAN J DE CALAZAN', u'JOSE DE CALASANZ'),
                (u'SAN JOSE CALAZANS', u'JOSE DE CALASANZ'),
                (u'SAN J DE CALANZANZ', u'JOSE DE CALASANZ'),
                (u'SAN JOSE DE CALASANZ', u'JOSE DE CALASANZ'),
                (u'SAN JOSE DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'S JOSE DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'S.J.DE CALASANZ', u'JOSE DE CALASANZ'),
                (u'S JOSE DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'S JOSE D CALAZANS', u'JOSE DE CALASANZ'),
                (u'S J0SE DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'S J DE CALAZANZ', u'JOSE DE CALASANZ'),
                (u'S J DE CALASANZ', u'JOSE DE CALASANZ'),
                (u'S J DE CALASAN', u'JOSE DE CALASANZ'),
                (u'S J D CALAZANS', u'JOSE DE CALASANZ'),
                (u'S J CALAZANS', u'JOSE DE CALASANZ'),
                (u'S J DE CALAZANS', u'JOSE DE CALASANZ'),
                (u'S J CALASANZ', u'JOSE DE CALASANZ'),
                (u'J DE CALASANZ', u'JOSE DE CALASANZ'),
                (u'AV JOSE DE CALASANZ', u'JOSE DE CALASANZ'),

                (u'NTA SRA DE LA CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA S DE LA CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA SRA D L CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA SRA DE CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA SRA DE L CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA SRA DELA CONSOLACION', u'DE LA CONSOLACION'),
                (u'NTRA STRA D L CONSOLACION', u'DE LA CONSOLACION'),

                (u'R J CARCANO', u'CARCANO'),
                (u'REYNA MONA', u'REYNA MORA'),
                (u'REINA MONA', u'REYNA MORA'),
                
                (u'AV LAS MALVINAS', u'MALVINAS'),
                (u'AV MALVINAS', u'MALVINAS'),
                (u'LAS MALVINAS', u'MALVINAS'),
                (u'MALVINAS ARGENTINAS', u'MALVINAS'),
                
                (u'S/N', u''),
                (u'N°', u' '),
                (u'-', u' ')))
    
    def clean(self, domicilio):
        for k in self.replaces.keys():
            domicilio = domicilio.replace(k, self.replaces[k])
            if domicilio == '': 
                domicilio = 'S/D'

        domicilio = domicilio.strip()
        domicilio = ' '.join(domicilio.split()) 

        lotes = ['(?P<prev>.*)(MZ|MZA|MZNA)(?P<manzana>[\s0-9]+)(LT|L|LOTE)(?P<lote>[\s0-9]+)(?P<pos>.*)', 
                 '(?P<prev>.*)(LT|L|LOTE)(?P<lote>[\s0-9]+)(MZ|MZA|MZNA)(?P<manzana>[\s0-9]+)(?P<pos>.*)']
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
                
        return domicilio
        