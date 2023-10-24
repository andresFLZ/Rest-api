from django.urls import path
from .views import TutorialView, UsuarioView, DetallesView

urlpatterns = [
    path('tutoriales/', TutorialView.as_view(), name='lista_tutoriales'), # Url para devover todos los turiales
    path('tutoriales/<int:id>', TutorialView.as_view(), name='tutorial'), # Url para devover un tutorial en especifico
    path('usuarios/', UsuarioView.as_view(), name='lista_usuarios'), # Url para devover todos los usuarios
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuario'), # Url para devover un usuario en especifico
    path('detalles/', DetallesView.as_view(), name='lista_detalles'), # Url para devover todos los detalles
    path('detalles/<int:id>', DetallesView.as_view(), name='detalle'), # Url para devover un detalle en especifico
]