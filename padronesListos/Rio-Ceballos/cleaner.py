# -*- coding: utf-8 -*-
from collections import OrderedDict
import re


class Cleaner():

    replaces = OrderedDict((
            (u'B°CENTRO-', u''),
            (u'B° NORTE-', u''),
            (u'B°CANTEGRIL-', u''),
            (u'B°LOS NOGALES(N)-', u''),
            (u'B° ÑU PORA-', u''),
            (u'B°ÑU PORA-', u''),
            (u'B°LA QUEBRADA-', u''),
            (u'B°LOZA-', u''),
            (u'B° LOZA-', u''),
            (u'B°A DEL PEÑON-', u''),
            (u'SGTO CABRAL', u'SARGENTO CABRAL'),
            (u'AV S MARTIN', u'SAN MARTIN'),
            (u'AV SAN MARTIN', u'SAN MARTIN'),
            (u'M PLANTE', u'MARIO PLANTE'),
            (u'CONCEJAL MARIO PLANTE', u'MARIO PLANTE'),
            (u'IPV MARIO PLANTE', u'MARIO PLANTE'),
            (u'B°IPV-MARIO PLANTE', u'MARIO PLANTE'),
            (u'AV 12 DE OCTUBRE', u'12 DE OCTUBRE'),
            (u'PJE 9 DE JULIO', u'9 DE JULIO'),
            (u'AV URUGUAY', u'URUGUAY'),
            (u'PJE COCHABAMBA', u'COCHABAMBA'),
            (u'B° LOS NOGALES N-CASTELLI', u'CASTELLI'),
            (u'1° DE MAYO', u'1 DE MAYO'),
            (u'1°DE MAYO', u'1 DE MAYO'),
            (u'RIO PILCOMAYO', u'PILCOMAYO'),
            (u'RAMON J CARCANO', u'CARCANO'),
            (u'J CARCANO', u'CARCANO'),
            (u'R J CARCANO', u'CARCANO'),
            (u'A LINCOLN', u'LINCOLN'),
            (u'ABRAHAM LINCOLN', u'LINCOLN'),
            (u'ABRAHAM LINCOL', u'LINCOLN'),
            (u'PJE ABRAHAM LINCOLN', u'LINCOLN'),
            (u'E SCHIAFFINO', u'SCHIAFFINO'),
            (u'ENRIQUE SCHIAFINO', u'SCHIAFFINO'),
            (u'F ALCORTA', u'FIGUEROA ALCORTA'),
            (u'D FUNES', u'DEAN FUNES'),
            (u'RIO BAMBA', u'BAMBA'),
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
                
        return domicilio