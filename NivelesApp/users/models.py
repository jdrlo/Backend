from typing import Any
from django.db import models
from django.contrib.auth.models import(AbstractBaseUser, PermissionsMixin, BaseUserManager)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Fatal email')
        user =self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff =True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    cargo = models.CharField(verbose_name=("Tipo Usuario"),choices=[('Mesero','Mesero'),('Dj','Dj'),('Proveedor','Proveedor'),('Administrador','Administrador'),('Cliente','Cliente')],default='Cliente')
    name= models.CharField(verbose_name= ("Nombre"), max_length=30)
    apellido_Usuario = models.CharField(verbose_name=("Apellido"), max_length=30)
    genero_Usuario = models.CharField(verbose_name=("Genero"),choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')])
    cedula = models.CharField(verbose_name=("Cedula"),null=True)
    telefono = models.CharField(verbose_name=("Telefono"),null=True)
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name
    
    
class Clientes(models.Model):
    id_Cliente= models.AutoField(primary_key=True)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User"))
    estado_Civil = models.CharField(verbose_name=("estado civil"), choices=[('Soltero','Soltero'),(('Comprometido','Comprometido'))])
    pregunta_Seguridad = models.CharField(verbose_name= ("Preguntas de Seguridad"), choices=[("nombre de tu mascota","nombre de tu mascota"),("color favorito","color favorito"),("colegio donde estudiaste","colegio donde estudiaste")], default=" - - - - - - - - - -")
    respuesta_Pregunta = models.CharField(verbose_name= ("Respuesta a Pregunta"), null=True)
    foto_Usuario = models.ImageField(verbose_name=("Foto Usuario"),null=True,blank=True, upload_to='imageUser/%Y%m/')
    match = models.CharField(verbose_name=("match"), choices=[('Si','Si'),('No','No')], default='No') #este campo tambien lo agregue
    
    