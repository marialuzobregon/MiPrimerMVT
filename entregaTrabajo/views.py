from bdb import GENERATOR_AND_COROUTINE_FLAGS
from configparser import ExtendedInterpolation
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from home.models import Familiar

def crear_familiar(request): 
    
    familiar1 = Familiar (nombre = 'Graciela', apellido = 'Videse', edad = '57', fecha_nacimiento = '1966-05-05')
    familiar1.save()
    familiar2  = Familiar (nombre = 'Luis', apellido = 'Obregon', edad = '68', fecha_nacimiento = '1955-02-02')
    familiar2.save()
    familiar3 = Familiar (nombre = 'Ramiro', apellido = 'Obregon', edad = '28', fecha_nacimiento = '1994-01-06')
    familiar3.save()
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar1':familiar1, 'familiar2': familiar2, 'familiar3': familiar3})
    
    return HttpResponse(template_renderizado)
    

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    
    return HttpResponse(template_renderizado)