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
        # Implememtación del método GET en el api para recuperar datos de Tutorial

        if (id > 0): # Devuele un tutorial en especifico dependiendo del id
            tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values())
            if len(tutoriales) > 0:
                tutorial = tutoriales[0]
                datos = {'message': "Success", 'company': tutorial}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else: # Devuelve todos los tutoriales 
            tutoriales = list(Tutorial.objects.values())
            if len(tutoriales) > 0:
                datos = {'message': "Success", 'companies': tutoriales}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # Implememtación del método POST en el api para registrar datos en Tutorial

        jd = json.loads(request.body)
        Tutorial.objects.create(titulo=jd['titulo'], descripcion=jd['descripcion'], estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    