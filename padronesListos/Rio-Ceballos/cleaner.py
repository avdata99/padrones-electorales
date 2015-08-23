# -*- coding: utf-8 -*-
from collections import OrderedDict
import re


class Cleaner():

    replaces = OrderedDict((
            (u'GRAL ', u'GENERAL '),
            (u'GRAL.', u'GENERAL'),
            (u'AVDA', u'AV'),
            (u'AVDA.', u'AV'),
            (u'AV.', u'AV'),
            (u'PJE ', u'PASAJE '),
            (u'PJE.', u'PASAJE'),
            (u'SGTO ', u'SARGENTO '),
            (u'SGTO.', u'SARGENTO '),
            (u'ALTE ', u'ALMIRANTE '),
            (u'CNEL ', u'CORONEL '),
            (u'ALTE.', u'ALMIRANTE'),
            (u'CNEL.', u'CORONEL'),
            (u'ING.', u'INGENIERO'),
            (u'ING', u'INGENIERO '),
            
            (u'B°CENTRO-', u''),
            (u'-B°CENTRO', u''),
            
            (u'B° NORTE-', u''),
            (u'B°CANTEGRIL-', u''),
            (u'B°LOS NOGALES(N)-', u''),
            (u'B°LA QUEBRADA-', u''),
            (u'B°S.MIGUEL-', u''),
            (u'-B°S.MIGUEL', u''),
            (u'B°HERBERA-', u''),
            (u'-B°HERBERA', u''),
            (u'B°AMISTAD-', u''),
            
            (u'B°LOZA-', u''),
            (u'B° LOZA-', u''),
            (u'-B°LOZA', u''),
            (u'-B° LOZA', u''),
            (u'BILOZA-', u''),
            (u'B°COLANCHANGA-', u''),
            
            (u'B° SANTA FE-', u''),
            
            (u'B°A DEL PEÑON-', u''),

            (u'B° ÑU PORA-', u''),
            (u'B°ÑU PORA-', u''),
            (u'-B°ÑUPORA', u''),
            (u'-B° ÑUPORA', u''),
            (u'B° PIETRI', u''),
            (u'B°PQUE ATALAYA-', u''),
            (u'B° EL CEDRO', u''),
            (u'B°AMUCHASTEGUI-', u''),
            (u'-B°AMUCHASTEGUI', u''),
            (u'B°PIETRI-', u''),
            (u'B°LA AMISTAD-', u''),
            (u'B°BELLA VISTA-', u''),
            (u'B°EL CEDRO-', u''),
            (u'B°MOREYRA-', u''),
            (u'B°SAN JOSE-', u''),
            
            
            
            (u'SGTO CABRAL', u'SARGENTO CABRAL'),
            (u'S CABRAL', u'SARGENTO CABRAL'),
            
            (u'AV S MARTIN', u'SAN MARTIN'),
            (u'AV SAN MARTIN', u'SAN MARTIN'),
            (u'AVENIDA SAN MARTIN', u'SAN MARTIN'),
            
            (u'M PLANTE', u'MARIO PLANTE'),
            (u'CONCEJAL MARIO PLANTE', u'MARIO PLANTE'),
            (u'IPV MARIO PLANTE', u'MARIO PLANTE'),
            (u'B°IPV-MARIO PLANTE', u'MARIO PLANTE'),
            (u'AV 12 DE OCTUBRE', u'12 DE OCTUBRE'),
            (u'PJE 9 DE JULIO', u'9 DE JULIO'),
            (u'PASAJE 9 DE JULIO', u'9 DE JULIO'),
            (u'AV URUGUAY', u'URUGUAY'),
            (u'PJE COCHABAMBA', u'COCHABAMBA'),
            (u'PASAJE COCHABAMBA', u'COCHABAMBA'),
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
            (u'PASAJE ABRAHAM LINCOLN', u'LINCOLN'),
            
            (u'ESCHIAFINO', u'SCHIAFFINO'),
            (u'ESCHAFINO', u'SCHIAFFINO'),
            (u'ESCHIAFFINO', u'SCHIAFFINO'),
            (u'SHIAFFINO', u'SCHIAFFINO'),
            (u'SCHAFINO', u'SCHIAFFINO'),
            (u'ECHIAFINO', u'SCHIAFFINO'),
            (u'SCHIAFINO', u'SCHIAFFINO'),
            (u'SCHAFFINO', u'SCHIAFFINO'),
            (u'SCHIARFINO', u'SCHIAFFINO'),
            
            (u'ENRIQYE', u'ENRIQUE'),
            
            (u'ENRIQUE SCHIAFFINO', u'SCHIAFFINO'),
            (u'E SCHIAFFINO', u'SCHIAFFINO'),
            (u'E.SCHIAFFINO', u'SCHIAFFINO'),
            
            (u'F ALCORTA', u'FIGUEROA ALCORTA'),
            (u'D FUNES', u'DEAN FUNES'),
            (u'RIO BAMBA', u'BAMBA'),
            (u'BME MITRE', u'MITRE'),
            (u'BARTOLOME MITRE', u'MITRE'),
            (u'B MITRE', u'MITRE'),
            (u'PJE BARTOLOME MITRE', u'MITRE'),
            (u'PASAJE BARTOLOME MITRE', u'MITRE'),
            (u'J J PASO', u'JUAN JOSE PASO'),
            (u'JUAN J PASO', u'JUAN JOSE PASO'),
            (u'J JOSE PASO', u'JUAN JOSE PASO'),
            (u'ALTE BROWN', u'ALMIRANTE BROWN'),
            (u'J B ALBERDI', u'ALBERDI'),
            (u'JUAN B ALBERDI', u'ALBERDI'),
            (u'JUAN BAUTISTA ALBERDI', u'ALBERDI'),
            (u'J BAUTISTA ALBERDI', u'ALBERDI'),
            (u'J ALBERDI', u'ALBERDI'),
            (u'B ALBERDI', u'ALBERDI'),
            (u'J L CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE LUIS CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'J L DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE A DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE L DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'J A DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JOSE L CPERONABRERA', u'JOSE LUIS DE CABRERA'),
            (u'J A CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'JO LUIS DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'PJE A DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'PASAJE A DE CABRERA', u'JOSE LUIS DE CABRERA'),
            (u'AVLOS INMIGRANTES', u'INMIGRANTES'),
            (u'AV LOS INMIGRANTES', u'INMIGRANTES'),
            (u'LOS INMIGRANTES', u'INMIGRANTES'),
            (u'L INMIGRANTES', u'INMIGRANTES'),

            (u'AV GENERAL MOSCONI', u'MOSCONI'),
            (u'GENERAL MOSCONI', u'MOSCONI'),
            (u'GENERAL E MOSCONI', u'MOSCONI'),
            (u'ENRIQUE MOSCONI', u'MOSCONI'),
            (u'E MOSCONI', u'MOSCONI'),
            (u'AV MOSCONI', u'MOSCONI'),
            (u'E.MOSCONI', u'MOSCONI'),
            (u'INGENIERO ENRIQUE MOSCONI', u'MOSCONI'),
            (u'INGENIERO E MOSCONI', u'MOSCONI'),
            (u'INGENIERO MOSCONI', u'MOSCONI'),
            (u'GENERAL. MOSCONI', u'MOSCONI'),
            
            
            (u'RDIOS DE ESCALADA', u'REMEDIOS DE ESCALADA'),
            
            (u'JUAN D PERON', u'PERON'),
            (u'GRAL PERON', u'PERON'),
            (u'GENERAL PERON', u'PERON'),
            (u'JUAN D PERON', u'PERON'),
            (u'JUAN DOMINGO PERON', u'PERON'),
            (u'JUAN PERON', u'PERON'),
            
            (u'S/N', u''),
            (u'N°', u' '),
            (u'-', u' '),
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