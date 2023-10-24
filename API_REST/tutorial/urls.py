from django.urls import path
from .views import TutorialList

app_name = 'tutorial'
urlpatterns = [
    path('', TutorialList.as_view(), name='Tutoriales'), # Url donde se podran ver listados los tutoriales
]