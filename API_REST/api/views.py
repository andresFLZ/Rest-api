from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Tutorial, Usuario, DetallesTutorial
import json
import requests


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
                datos = {'message': "Success", 'tutorial': tutorial}
            else:
                datos = {'message': "Tutorial no encontrado..."}
            return JsonResponse(datos)
        else: # Devuelve todos los tutoriales 
            tutoriales = list(Tutorial.objects.values()) # Recupera los tutoriales de la base de datos
            if len(tutoriales) > 0:
                datos = {'message': "Success", 'tutoriales': tutoriales}
            else:
                datos = {'message': "Tutoriales no encontrados..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # Implememtación del método POST en la api para registrar un nuevo tutorial

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
    
    def delete(self, request, id):
        # Implememtación del método DELETE en la api para eliminar datos de Tutorial

        tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values()) # Recupera el tutorial de la base de datos
        if len(tutoriales) > 0:
            Tutorial.objects.filter(id_tutorial=id).delete() # Elimina el tutorial de la base de datos
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tutorial no encontrado..."}
        return JsonResponse(datos)
    
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Función encargada de permitir los envios POST ignorando el csrf

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        # Implememtación del método GET en la api para recuperar datos de Usuario

        if (id > 0): # Devuele un usuario en especifico dependiendo del id
            usuarios = list(Usuario.objects.filter(id_usuario=id).values()) # Recupera el usuario de la base de datos
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Success", 'usuario': usuario}
            else:
                datos = {'message': "Usuario no encontrado..."}
            return JsonResponse(datos)
        else: # Devuelve todos los usuarios 
            usuarios = list(Usuario.objects.values()) # Recupera los usuarios de la base de datos
            if len(usuarios) > 0:
                datos = {'message': "Success", 'usuarios': usuarios}
            else:
                datos = {'message': "usuarios no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        # Implememtación del método POST en la api para registrar usuarios 

        jd = json.loads(request.body) # Recupera los datos del request
        Usuario.objects.create(nombres=jd['nombres'], apellidos=jd['apellidos']) # Crea un usuario en la base de datos
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
class DetallesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Función encargada de permitir los envios POST ignorando el csrf

        return super().dispatch(request, *args, **kwargs)
    
    def recuperarTutorial(self, id):
        tutoriales = list(Tutorial.objects.filter(id_tutorial=id).values()) # Recupera el tutorial de la base de datos
        if len(tutoriales) > 0:
            return Tutorial.objects.get(id_tutorial=id) # este es el tutorial que se va a asociar con el detalle
        
    def recuperarUsuario(self, id):
        usuarios = list(Usuario.objects.filter(id_usuario=id).values()) # Recupera el usuario de la base de datos
        if len(usuarios) > 0:
            return Usuario.objects.get(id_usuario=id) # este es el usuario que se va a asociar con el detalle

    def get(self, request, id=0):
        # Implememtación del método GET en la api para recuperar detalles asociados a los tutoriales

        if (id > 0): # Devuele un detalle en especifico dependiendo del id
            detalles = list(DetallesTutorial.objects.filter(id_detalles=id).values()) # Recupera el detalle de la base de datos
            if len(detalles) > 0:
                detalle = detalles[0]
                datos = {'message': "Success", 'detalle': detalle}
            else:
                datos = {'message': "Detalle no encontrado..."}
            return JsonResponse(datos)
        else: # Devuelve todos los detalles 
            detalles = list(DetallesTutorial.objects.values()) # Recupera los detalles de la base de datos
            if len(detalles) > 0:
                datos = {'message': "Success", 'detalles': detalles}
            else:
                datos = {'message': "Detalles no encontrados..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # Implememtación del método POST en la api para registrar un nuevo detalle

        jd = json.loads(request.body) # Recupera los datos del request
        tutorial = self.recuperarTutorial(jd['id_tutorial'])
        usuario = self.recuperarUsuario(jd['id_usuario_creador'])

        DetallesTutorial.objects.create(id_tutorial=tutorial, usuario_creador=usuario) # Crea un detalle en la base de datos
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        # Implememtación del método PUT en la api para actualizar datos de un detalle asociado a un tutorial

        jd = json.loads(request.body) # Recupera los datos del request
        tutorial = self.recuperarTutorial(jd['id_tutorial']) # Esté es el tutorial nuevo
        usuario = self.recuperarUsuario(jd['id_usuario_creador']) # Esté es el usuario nuevo
        print(tutorial, usuario)
        detalles = list(DetallesTutorial.objects.filter(id_detalles=id).values())
        if len(detalles) > 0:
            detalle = DetallesTutorial.objects.get(id_detalles=id) # Recupera el detalle de un tutorial de la base de datos
            detalle.id_tutorial = tutorial
            detalle.usuario_creador = usuario
            detalle.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no encontrado..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        # Implememtación del método DELETE en la api para eliminar un detalle asociado a un tutorial

        detalles = list(DetallesTutorial.objects.filter(id_detalles=id).values()) # Recupera el detalle de la base de datos
        if len(detalles) > 0:
            DetallesTutorial.objects.filter(id_detalles=id).delete() # Elimina el detalle de la base de datos
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tutorial no encontrado..."}
        return JsonResponse(datos)