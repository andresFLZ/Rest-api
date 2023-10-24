from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import random
from .forms import TutorialForm
from api.models import DetallesTutorial, Tutorial, Usuario

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
    # Vista encargada de mostrar la lista de todos los tutoriales

    model = Tutorial
    template_name = 'tutorial/tutorial_form.html'
    form_class = TutorialForm
    #second_form_class = Tutorial
    success_url = reverse_lazy('tutorial:Tutoriales')
    
    def crearDetalle(self, tutorial):
        # Esté método crea el detalle asociado al tutorial
        detalles = DetallesTutorial()
        detalles.id_tutorial = tutorial
        detalles.usuario_creador = list(Usuario.objects.filter())[random.randint(1, Usuario.objects.count())-1] # Se asigna un usuario al azar de los usuarios en la base de datos

        detalles.save()

    def post(self, request, *args, **kwargs):
        # Se sobreescribe el método post para que no solo cree el tutorial sino también el detalle de ese tutorial

        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            tutorial = form.save() # Se crea el tutorial
            self.crearDetalle(tutorial) # Se crea el detalle asociado
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class TutorialUpdate(UpdateView):
    # Vista encargada de mostrar el formulario de modificación de un tutorial

    model = Tutorial
    template_name = 'tutorial/tutorial_form.html'
    form_class = TutorialForm
    success_url = reverse_lazy('tutorial:Tutoriales')

class TutorialDelete(DeleteView):
    # Vista encargada de mostrar la confirmación de eliminación de un tutorial

    model = Tutorial
    template_name = 'tutorial/tutorial_confirm_delete.html'
    success_url = reverse_lazy('tutorial:Tutoriales')