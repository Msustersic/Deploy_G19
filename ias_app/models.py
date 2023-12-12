from django.db import models
from django.db.models import Model 
'''
   al importar así, no se referencia al module models en la herencia de clases
   class MiClase(models.Model), es decir:
   class MiClase(Model)
'''
class IaFunction(Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(blank=False,null=False,max_length=30)
   image = models.CharField(blank=False,null=False,max_length=30)
   
   class Meta:
      db_table = "t_ia_function"
   
   def __str__(self):
      return f"{self.nombre}, {self.image}"
   
   def get_fields(self):
      return [
         (field.verbose_name, field.value_from_object(self))
         for field in self.__class__._meta.fields[1:]
      ]

class Ia(Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(blank=False,null=False,max_length=50)
   image = models.CharField(blank=False,null=False,max_length=60)
   link = models.CharField(blank=False,null=False,max_length=255)
   functionList = models.ManyToManyField(IaFunction)
   
   class Meta:
      db_table = "t_ias"
   
   def __str__(self):
      functionList_str = ', '.join([str(function) for function in self.functionList.all()])
      return f'nombre de IA: {self.nombre}, funcionalidades: {functionList_str}'
   
   def get_fields(self):
      return [
         (field.verbose_name, field.value_from_object(self))
         for field in self.__class__._meta.fields[1:]
      ]

class Comment(Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(blank=False,null=False,max_length=50)
   email = models.EmailField(blank=False,null=False,max_length=60)
   comentario = models.CharField(blank=False,null=False,max_length=255)
   fecha = models.DateField(auto_now=True)

   class Meta:
      db_table = "t_comments"
   
   def __str__(self):
      return f'fecha: {self.fecha}, nombre: {self.nombre}, commentario: {self.comentario}'
   
   def get_fields(self):
      return [
         (field.verbose_name, field.value_from_object(self))
         for field in self.__class__._meta.fields[1:]
      ]

class Curso(Model):
   institucion = models.CharField(blank=False,null=False,max_length=30,default="Codo a Codo")
   curso = models.CharField(blank=False,null=False,max_length=30,default="Full-Stack Python 2023")
   grupo = models.PositiveSmallIntegerField(blank=False,null=False,default=19)
   comision = models.PositiveSmallIntegerField(blank=False,null=False,default=23507)
   
   class Meta:
      db_table = "t_cursos"
   
   def __str__(self):
      return f"institución: {self.institucion}, curso: {self.curso}, grupo: {self.grupo}, comisión: {self.comision}"
   
   def get_fields(self):
      return [
         (field.verbose_name, field.value_from_object(self))
         for field in self.__class__._meta.fields[1:]
      ]
   
class Alumno(Model):   
   nombres = models.CharField(blank=False,null=False,max_length=30)
   apellidos = models.CharField(blank=False,null=False,max_length=30)
   email = models.EmailField(blank=False,null=False,max_length=50)
   movil = models.CharField(blank=False,null=False,max_length=13)
   github = models.CharField(blank=False,null=False,max_length=30)
   
   class Meta:
      db_table = "t_alumnos"
   
   def __str__(self):
      return f"nombre y apellido: {self.nombre} {self.apellido},\
         email: {self.email}, movil: {self.movil}, github: {self.github}"
   
   def get_fields(self):
      return [
         (field.verbose_name, field.value_from_object(self))
         for field in self.__class__._meta.fields[1:]
      ]
