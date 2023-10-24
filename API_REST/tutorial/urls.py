from django.urls import path
from .views import TutorialList, TutorialCreate, TutorialUpdate, TutorialDelete

app_name = 'tutorial'
urlpatterns = [
    path('', TutorialList.as_view(), name='Tutoriales'), # Url donde se podran ver listados los tutoriales
    path('nuevo/', TutorialCreate.as_view(), name='Crear'), # Url donde se podran ver listados los tutoriales
    path('editar/<int:pk>/', TutorialUpdate.as_view(), name='Editar'), # Url donde se podran modificar los tutoriales
    path('eliminar/<int:pk>/', TutorialDelete.as_view(), name='Eliminar'), # Url donde se podran eliminar los tutoriales
]