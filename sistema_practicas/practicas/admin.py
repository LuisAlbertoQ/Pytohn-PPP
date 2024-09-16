from django.contrib import admin
from .models import Usuario, Estudiante, Empresa, Supervisor, Practica, Evaluacion

admin.site.register(Usuario)
admin.site.register(Estudiante)
admin.site.register(Empresa)
admin.site.register(Supervisor)
admin.site.register(Practica)
admin.site.register(Evaluacion)
