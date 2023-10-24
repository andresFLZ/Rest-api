from django.urls import path
from .views import TutorialView

urlpatterns = [
    path('tutoriales/', TutorialView.as_view(), name='lista_tutoriales'), # Url para devover todos los turiales
    path('tutoriales/<int:id>', TutorialView.as_view(), name='tutorial'), # Url para devover un tutorial en especifico
]