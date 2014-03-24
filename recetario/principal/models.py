from django.db import models
class Bebida(models.Model):
 nombre = models.CharField(max_length=50)
 ingredientes = models.TextField()
 preparacion = models.TextField()
 def __unicode__(self):
  return self.nombre
class Proyecto(models.Model):
    nombre= models.CharField(max_length=50)
    codigo= models.IntegerField(max_length=20)
    def __unicode__(self):
        return self.nombre


