from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'supervisores', views.SupervisorViewSet)
router.register(r'practicas', views.PracticaViewSet)
router.register(r'evaluaciones', views.EvaluacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
