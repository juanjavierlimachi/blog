from django.db import models

# Create your models here.
from django.contrib.auth.forms import User
# Create your models here.
class Perfiles(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfil')
	materno = models.CharField(max_length=50)
	ci = models.IntegerField()
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username

class Alumnos(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfilAlumno')
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username
	
class Directores(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfilDirector')
	materno = models.CharField(max_length=50)
	ci = models.IntegerField()
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username
class Producto(models.Model):
	Nombre_producto=models.CharField(max_length=150, unique=True)
	Descripcion=models.TextField()
	usuario = models.ForeignKey(User)
	Precio_Venta=models.FloatField()
	#Precio_Compra=models.FloatField()#precio compra
	#Stock = models.IntegerField(default=0)
	estado = models.BooleanField(default=True)
	Imagen = models.FileField(upload_to = 'imagenes',blank=True, null=True)
	fecha_registro=models.DateTimeField(auto_now=True)
	En_oferta = models.BooleanField(default=False)
	def __unicode__(self):
		return self.Nombre_producto