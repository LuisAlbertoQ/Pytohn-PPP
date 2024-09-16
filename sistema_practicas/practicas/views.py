from rest_framework import viewsets
from .models import Usuario, Estudiante, Empresa, Supervisor, Practica, Evaluacion
from .serializers import UsuarioSerializer, EstudianteSerializer, EmpresaSerializer, SupervisorSerializer, PracticaSerializer, EvaluacionSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    permission_classes = [IsAdminUser]

class PracticaViewSet(viewsets.ModelViewSet):
    queryset = Practica.objects.all()
    serializer_class = PracticaSerializer
    permission_classes = [IsAuthenticated]

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
