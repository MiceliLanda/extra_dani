from django.db import models

# Create your models here.

class ModelRegistro(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apPat = models.CharField(max_length=254,null=False)
    apMat = models.CharField(max_length=254,null=False)
    edad = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre,self.apPat,self.apMat,self.edad
        

    class Meta:
        db_table = 'Personas'