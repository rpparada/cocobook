import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','cocobook.settings')

import django
django.setup()

import random
from datetime import date
from preinscripcion.models import UsuarioPreIns, PlanPreIns
from faker import Faker

fakegen = Faker()

nombre_planes = [('Super plan 1','Descripcion super plan 1'),('Super plan 2','Descripcion super plan 2'),('Super plan 3','Descripcion super plan 1')]

def agrega_plan():
    plan,desc = random.choice(nombre_planes)
    p = PlanPreIns.objects.get_or_create(
                        nombre=plan,
                        descripcion=desc,
                        valor=random.randint(1000,2000),
                        fecha_creacion=fakegen.date())[0]
    p.save()
    return p

def agregar_usuario(N=10):

    for num in range(N):
        plan = agrega_plan()
        nom_falso = fakegen.name()
        email_falso = fakegen.email()
        numtel_falso = fakegen.phone_number()

        user = UsuarioPreIns.objects.get_or_create(
                        nombre=nom_falso,
                        email=email_falso,
                        numero_telefonico = numtel_falso,
                        rut='1-9',
                        numero_hijos=3,
                        fecha_creacion=fakegen.date())[0]
        user.save()

if __name__ == '__main__':
    print('comienza')
    agregar_usuario()
    print('fin')
