from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('estudiante', 'Estudiante'), ('supervisor', 'Supervisor'), ('empresa', 'Empresa')])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)
    semestre = models.IntegerField()
    universidad = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.carrera}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    representante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Supervisor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.especialidad}"

class Practica(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    horas_totales = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('en curso', 'En curso'), ('completada', 'Completada')], default='pendiente')
    
    def completar_practica(self):
        """Completa la práctica si ya tiene una evaluación asociada"""
        if self.evaluacion:
            self.estado = 'completada'
            self.save()
            
    def __str__(self):
        return f"Práctica de {self.estudiante.usuario.nombre} en {self.empresa.nombre}"

class Evaluacion(models.Model):
    practica = models.OneToOneField(Practica, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField()
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    comentarios = models.TextField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guardar la evaluación
        self.practica.completar_practica()  # Completar la práctica asociada

    def __str__(self):
        return f"Evaluación de {self.practica.estudiante.usuario.nombre}"
