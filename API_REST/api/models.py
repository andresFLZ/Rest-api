from django.db import models

class Tutorial(models.Model):
    #Modelo de la tabla Tutorial para la base de datos

    id_tutorial = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(verbose_name='descripción')
    estado = models.BooleanField(default=False)

    #Información principal de la tabla Tutorial
    class Meta:
        db_table = 'Tutorial'
        verbose_name = 'tutorial'
        verbose_name_plural = 'tutoriales'

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    #Modelo de la tabla Usuario para la base de datos

    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    #Información principal de la tabla Usuario
    class Meta:
        db_table = 'Usuario'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.nombres + " " + self.apellidos
    
class DetallesTutorial(models.Model):
    #Modelo de la tabla DetallesTutorial para la base de datos

    id_detalles = models.AutoField(primary_key=True)
    dia_creacion = models.DateTimeField(auto_now_add=True, verbose_name='día de creación')
    id_tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, verbose_name='tutorial'
    )# Relación uno a muchos con la tabla Tutorial
    usuario_creador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name='usuario'
    )# Relación uno a muchos con la tabla Usuario

    #Información principal de la tabla DetallesTutorial
    class Meta:
        db_table = 'DetallesTutorial'
        verbose_name = 'detalles del tutorial'
        verbose_name_plural = 'detalles de los tutoriales'

    def __str__(self):
        return self.dia_creacion