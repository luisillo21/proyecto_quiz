from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    nombre_usuario = models.CharField(max_length=100,null=False,blank=False)
    clave = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.nombre_usuario

    class Meta:
        verbose_name = 'Autor',
        verbose_name_plural = 'Autores',
        db_table = 'usuario'


class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=False, blank=False,related_name='autor_del_examen',db_column='id_usuario')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Examen',
        verbose_name_plural = 'Examenes',
        db_table = 'examen'



class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.TextField(max_length=200,null=False,blank=False)
    opcion1 = models.CharField(max_length=50,null=False,blank=False)
    opcion2 = models.CharField(max_length=50, null=False,blank=False)
    respuesta = models.CharField(max_length=50, null=False,blank=False)
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE,related_name='preguntas_del_examen', db_column='id_examen')

    def __str__(self):
        return self.pregunta

    class Meta:
        verbose_name = 'Pregunta',
        verbose_name_plural = 'Preguntas',
        db_table = 'preguntas'