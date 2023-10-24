from django.urls import path
from .views import TutorialList, TutorialCreate

app_name = 'tutorial'
urlpatterns = [
    path('', TutorialList.as_view(), name='Tutoriales'), # Url donde se podran ver listados los tutoriales
    path('nuevo/', TutorialCreate.as_view(), name='Crear'), # Url donde se podran ver listados los tutoriales
]