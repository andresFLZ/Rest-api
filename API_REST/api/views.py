from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Tutorial, Usuario, DetallesTutorial
import json


class TutorialView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Función encargada de permitir los envios POST ignorando el csrf

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        # Implememtación del método GET en la api para recuperar datos de Tutorial

        if (id > 0): # Devuele un tutorial en especifico dependiendo del id
            tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values()) # Recupera el tutorial de la base de datos
            if len(tutoriales) > 0:
                tutorial = tutoriales[0]
                datos = {'message': "Success", 'company': tutorial}
            else:
                datos = {'message': "Tutorial no encontrado..."}
            return JsonResponse(datos)
        else: # Devuelve todos los tutoriales 
            tutoriales = list(Tutorial.objects.values()) # Recupera los tutoriales de la base de datos
            if len(tutoriales) > 0:
                datos = {'message': "Success", 'companies': tutoriales}
            else:
                datos = {'message': "Tutoriales no encontrados..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # Implememtación del método POST en la api para registrar datos en Tutorial

        jd = json.loads(request.body) # Recupera los datos del request
        Tutorial.objects.create(titulo=jd['titulo'], descripcion=jd['descripcion'], estado=jd['estado']) # Crea un tutorial en la base de datos
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        # Implememtación del método PUT en la api para actualizar datos de Tutorial

        jd = json.loads(request.body) # Recupera los datos del request
        tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values())
        if len(tutoriales) > 0:
            tutorial = Tutorial.objects.get(id_tutorial=id) # Recupera el tutorial de la base de datos
            tutorial.titulo = jd['titulo']
            tutorial.descripcion = jd['descripcion']
            tutorial.estado = jd['estado']
            tutorial.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tutorial no encontrado..."}
        return JsonResponse(datos)