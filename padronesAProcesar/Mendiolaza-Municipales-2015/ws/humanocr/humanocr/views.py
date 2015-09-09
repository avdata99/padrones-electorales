# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import glob
# import os




def ver(request):
    sdir = settings.BASEF
    path_pbms = '%s/processing/*.png' % sdir
    # archives = os.listdir(path_pbms)
    archives = glob.glob(path_pbms)
    
    # los pares de una forma y los imapares de otra
    context = {'archives': [x.split('/')[-1:][0] for x in archives]}
    return render(request, 'ver.html', context)
    