# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import glob
# import os




def ver(request):
    path_pbms = '%s/*.png' % settings.PROCESSINGF
    # archives = os.listdir(path_pbms)
    archives = glob.glob(path_pbms)
    
    pngs = sorted([x.split('/')[-1:][0].replace('.png', '') for x in archives])
    context = {'archives': pngs}
    return render(request, 'ver.html', context)
    