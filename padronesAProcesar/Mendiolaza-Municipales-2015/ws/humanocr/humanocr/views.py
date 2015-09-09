# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import glob
import os
from models import Elector
from django.core.exceptions import ObjectDoesNotExist


def ver(request, tipo='nombre', pagina='66'):
    path_pbms = '%s/%s/%s*page-%s.png' % (settings.BASEF, '323pages', tipo, pagina) # settings.PROCESSINGF
    # archives = os.listdir(path_pbms)
    archives = glob.glob(path_pbms)
    
    pngs = sorted([x.split('/')[-1:][0].replace('.png', '') for x in archives])
    context = {'archives': pngs, 'tipo': tipo, 'pagina': pagina}
    return render(request, 'ver.html', context)

def getImage(request, tipo, orden, pagina, columna):
    """ fuck staticfiles! """
    img_file = '%s/%s/%s-%s-col%s-page-%s.png' % (settings.BASEF, '323pages', tipo, orden, columna, pagina)
    image_data = open(img_file, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

def getText(request, tipo, orden, pagina, columna):
    """ fuck staticfiles! """
    txt_file = '%s/%s/%s-%s-col%s-page-%s.png.txt' % (settings.BASEF, '323pages', tipo, orden, columna, pagina)
    text_data = open(txt_file, "rb").read()
    value=text_data.replace('\n', '')
    value=value.replace('\r', '')
    value=value.replace('  ', ' ')
    value=value.strip()
    value=value.lower()
    value=value.replace('á', 'a')
    value=value.replace('é', 'e')
    value=value.replace('í', 'i')
    value=value.replace('ó', 'o')
    value=value.replace('ú', 'u')

    value=value.replace('Á', 'a')
    value=value.replace('É', 'e')
    value=value.replace('Í', 'i')
    value=value.replace('Ó', 'o')
    value=value.replace('Ú', 'u')

    if tipo == 'dni':
        value=value.replace(' ', '')
        value=value.replace('o', '0')
        value=value.replace('l', '1')
        value=value.replace('.', '')
        value=value.replace('_', '')
        
        
    
    return HttpResponse(value, mimetype="text/plain")

def setText(request):
    """ grabar como texto definitivo en la ubicacion que le corresponde """

    value = request.POST['value']
    tipo= request.POST['tipo']
    orden= request.POST['orden']
    pagina= request.POST['pagina']
    columna= request.POST['columna']

    value=value.replace('\n', '')
    value=value.replace('\r', '')
    value=value.replace('  ', ' ')
    value=value.strip()
    if tipo=='dni' and value=='': value=0


    try:
        e = Elector.objects.get(pagina=pagina, columna=columna,orden=orden)
    except ObjectDoesNotExist:
        e = None
        
    if not e:
        e = Elector(pagina=pagina, columna=columna,orden=orden)
        e.save()

    setattr(e, tipo, value)
    e.save()
        
    # finalmente borrar para que no aparezca
    txt_file = '%s/%s/%s-%s-col%s-page-%s.png.txt' % (settings.BASEF, '323pages', tipo, orden, columna, pagina)
    img_file = '%s/%s/%s-%s-col%s-page-%s.png' % (settings.BASEF, '323pages', tipo, orden, columna, pagina)
    os.remove(txt_file)
    os.remove(img_file)
    
    return HttpResponse('{"status": "OK"}', mimetype="application/json")