from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Tutorial, Usuario, DetallesTutorial
import json


class TutorialView(View):

    def get(self, request, id=0):
        if (id > 0):
            tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values())
            if len(tutoriales) > 0:
                tutorial = tutoriales[0]
                datos = {'message': "Success", 'company': tutorial}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else:
            tutoriales = list(Tutorial.objects.values())
            if len(tutoriales) > 0:
                datos = {'message': "Success", 'companies': tutoriales}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)

    