from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import TutorialForm
from api.models import DetallesTutorial, Tutorial

class TutorialList(ListView):
    # Vista encargada de mostrar la lista de todos los tutoriales

    model = Tutorial
    template_name = 'tutorial/tutorial_list.html' # Esté es el html donde estaran los tutoriales
    context_object_name = 'tutorial_list'

    def get_context_data(self, **kwargs):
        # Está función se encarga de agregar los detalles asociados al tutorial al contexto de la solicitud

        context = super().get_context_data(**kwargs)
        context['detalle_tutorial'] = DetallesTutorial.objects.all()
        return context
    
class TutorialCreate(CreateView):
    model = Tutorial
    template_name = 'tutorial/tutorial_form.html'
    form_class = TutorialForm
    success_url = reverse_lazy('tutorial:Tutoriales')