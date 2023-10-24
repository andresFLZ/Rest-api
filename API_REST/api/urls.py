from django.urls import path
from .views import TutorialView

urlpatterns = [
    path('tutoriales/', TutorialView.as_view(), name='lista_tutoriales'),
    path('tutoriales/<int:id>', TutorialView.as_view(), name='tutorial')
]