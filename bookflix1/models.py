from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tarjeta(models.Model):
    num=models.IntegerField(blank=False, null=False)
    cod=models.IntegerField(blank=False, null=False)
    nom=models.CharField(max_length=30,blank=False,verbose_name='Nombre')
    venc=models.DateField(blank=False,null=True,verbose_name='Fecha')

    def __str__(self):
        cadena=str(self.num)
        return cadena

class Precio(models.Model):
    fecha=models.DateField(blank=False,null=True,verbose_name='Fecha')
    tipo=models.CharField(max_length=250,verbose_name='Tipo')
    costo=models.IntegerField(blank=False,null=True,verbose_name='Costo')
    
    def __str__(self):
        cadena=self.tipo
        return cadena

class Usuario(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    #nombre=models.CharField(max_length=30,blank=False,verbose_name='Nombre')
    #pellido=models.CharField(max_length=30,blank=False,verbose_name='Apellido')
    #email=models.EmailField(unique=True,max_length=100,blank=False,verbose_name='Email')
    #password=models.CharField(max_length=250, blank=False,null=False,verbose_name='Password')
    dni=models.CharField(blank=False, unique=True, max_length=8,verbose_name='DNI')
    nacimiento=models.DateField(blank=False,null=True,verbose_name='Nacimiento')
    tarjeta=models.ForeignKey(Tarjeta, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Tarjeta de Credito')
    tipo=models.ForeignKey(Precio,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        cadena=self.user.username
        return cadena

class Perfil(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    nom=models.CharField(max_length=15,verbose_name='Nombre')
    fecha=models.DateField(blank=False,null=True,verbose_name='Fecha')

    def __str__(self):
        cadena=self.nom
        return cadena

class Editorial(models.Model):
    nombre=models.CharField(max_length=50,blank=False,null=True,verbose_name='Nombre')

    def __str__(self):
        cadena=self.nombre
        return cadena

class Autor(models.Model):
    nombre=models.CharField(max_length=25,blank=False,null=True,verbose_name='Nombre')
    nacimiento=models.DateField(blank=False,null=True,verbose_name='Fecha de Nacimiento')

    def __str__(self):
        cadena=self.nombre
        return cadena


class Genero(models.Model):
    nombre=models.CharField(max_length=250,blank=False,null=True,verbose_name='Nombre')

    def __str__(self):
        cadena=self.nombre
        return cadena

class Novedad(models.Model):
    titulo=models.CharField(max_length=250,blank=False,null=True,verbose_name='Titulo')
    descripcion=models.CharField(max_length=250,blank=False,null=True,verbose_name='Descripcion')


class Libro(models.Model):
    titulo=models.CharField(max_length=250,blank=False,null=True,verbose_name='Titulo')
    trailer=models.CharField(max_length=500,blank=False,null=True,verbose_name='Trailer')
    capitulado=models.BooleanField(blank=False,null=True,verbose_name='Es Capitulado')
    autor=models.ForeignKey(Autor, on_delete=models.SET_NULL,null=True)
    editorial=models.ForeignKey(Editorial, on_delete=models.SET_NULL,null=True)
    genero=models.ForeignKey(Genero, on_delete=models.SET_NULL,null=True)
    pdf=models.FileField(upload_to="librosCompletos",null=True)
    def __str__(self):
        cadena=self.titulo + "  -  " + self.autor.nombre
        return cadena

class Comentario(models.Model):
    texto=models.CharField(max_length=250,blank=False,null=True,verbose_name='Texto')
    autor=models.ForeignKey(Perfil, on_delete=models.SET_NULL,null=True)
    libro=models.ForeignKey(Libro,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        cadena=self.texto
        return cadena

class Calificacion(models.Model):
    cuanto=models.IntegerField(blank=False,null=True,verbose_name='Valor')
    autor=models.ForeignKey(Perfil, on_delete=models.SET_NULL,null=True)
    libro=models.ForeignKey(Libro,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        cadena=str(self.cuanto)
        return cadena

class Busqueda(models.Model):
    fecha=models.DateField(blank=False,null=True)
    quien=models.ForeignKey(Perfil,on_delete=models.SET_NULL,null=True)
    que=models.CharField(blank=False,null=True,max_length=200)


class Capitulo(models.Model):
    numero=models.IntegerField(null=False,blank=False)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE,null=True)
    pdf=models.FileField(upload_to='pdf',verbose_name="Archivo PDF",null=True)