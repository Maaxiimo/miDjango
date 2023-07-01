from django.db import models

# Create your models here.

class Estado (models.Model):
    idestado = models.IntegerField(primary_key=True, verbose_name= "id de estado " )
    nombreestado =   models.CharField(max_length=25,verbose_name="Nombre de estado" , blank= False)

    def __str__(self):
        return  self.nombreestado
    
class Rol (models.Model):
    idrol = models.IntegerField(primary_key=True, verbose_name= "id de rol ") 
    nombrerol = models.CharField(max_length=25,verbose_name="Nombre de rol", blank= False) 

    def __str__(self):
        return  self.nombrerol
    
class Pelicula(models.Model):
    idpelicula = models.AutoField(primary_key=True,verbose_name="codigo de la pelicula")
    nombrepelicula = models.CharField(max_length=45,verbose_name="Nombre de la pelicula", blank= False)
    director = models.CharField (max_length=30 , verbose_name="Nombre del director" , blank = False)
    reparto =  models.CharField (max_length=50 , verbose_name="Nombres del reparto principal de la pelicula" , blank = False )
    descripcion =  models.CharField (max_length=100 , verbose_name="descripcion de la pelicula" , blank = False)
    imagen = models.ImageField(upload_to="peliculasimagen", null = True)

    def __str__(self):
        return  self.nombrepelicula
    

class Cuenta (models.Model):
    idcuenta =  models.AutoField(primary_key=True,verbose_name="codigo de la cuenta")
    usuario = models.CharField(max_length=25,verbose_name="Nombre de la cuenta", blank= False)
    correo = models.CharField(max_length=45,verbose_name="correo electronico", blank= False)
    contraseña = models.CharField(max_length=30,verbose_name="contraseña", blank=False)
    rol = models.ForeignKey(Rol , on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado , on_delete=models.CASCADE)

    def __str__(self):
        return  self.usuario
    
class Calificacion (models.Model):
    idcalificacion = models.IntegerField(primary_key=True , verbose_name= "id calificacion")
    puntuacion = models.IntegerField (verbose_name= "puntuacion de la persona a la pelicula" , blank=True)
    comentario = models.CharField(max_length=70,verbose_name="comentarios a la pelicula", blank=True  )
    pelicula = models.ForeignKey(Pelicula , on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta , on_delete=models.CASCADE)

    def __str__(self):
        return  self.puntuacion
    
class Categoria (models.Model):
    idcategoria =  models.IntegerField(primary_key=True,verbose_name="id de la categoria")
    nombrecategoria =  models.CharField(max_length=45,verbose_name="Nombre de las categorias", blank=False )

    def __str__(self):
        return  self.nombrecategoria
    
class  Categoriapelicula (models.Model):
    idtiposcategoria = models.IntegerField(primary_key=True, verbose_name= "id de todas las categorias de cada peliculas") 
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)

    def ___str___(self):
        return  self.idtiposcategoria