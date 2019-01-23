from django.db import models

# Create your models here.
class PlanPreIns(models.Model):
    nombre = models.CharField(max_length=254,unique=False)
    descripcion = models.CharField(max_length=254,unique=False)
    valor = models.IntegerField()

    clave_pri = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre

class UsuarioPreIns(models.Model):
    nombre = models.CharField(max_length=254,unique=False)
    email = models.EmailField(max_length=254,unique=False)
    numero_telefonico = models.CharField(max_length=50,unique=False)
    rut = models.CharField(max_length=50,unique=False)
    numero_hijos = models.SmallIntegerField()

    plan_preferido = models.ForeignKey(PlanPreIns,on_delete=models.CASCADE)


    clave_pri = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre
