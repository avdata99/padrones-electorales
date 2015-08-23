# -*- coding: utf-8 -*-
from collections import OrderedDict
import re


class Cleaner():

    replaces = OrderedDict((
            (u'jerónimo', u'jeronimo'),
            (u'J LUIS DE CABRERA', u'jeronimo luis de cabrera'),
            (u'jeronimo l de cabrera', u'jeronimo luis de cabrera'),
            (u'j l de cabrera', u'jeronimo luis de cabrera'),
            (u'g l de cabrera', u'jeronimo luis de cabrera'),
            (u'chacabuco la cruz', u'chacabuco'),
            (u'bindustrial chacabuco', u'chacabuco'),
            (u'la cruz chacabuco', u'chacabuco'),
            (u'industrial chacabuco', u'chacabuco'),
            (u'bla cruz chacabuco', u'chacabuco'),
            (u'chacabuco industrial', u'chacabuco'),
            (u'p de los andes', u'paso de los andes'),
            (u'bcruz paso de los andes', u'paso de los andes'),
            (u'paso de los andes la cruz', u'paso de los andes'),
            (u'blomas barcelona', u'barcelona'),
            (u'blomas sur barcelona', u'barcelona'),
            (u'd quiros', u'duarte quiros'),
            
            
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
                
        return domicilio