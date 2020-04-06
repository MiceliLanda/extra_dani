from django.shortcuts import render
from rest_framework import views
from Personas.models import ModelRegistro
from Personas.serializer import PersonasSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 

class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

@csrf_exempt
def lista_personas(request):
    if request.method == 'GET':
        personas = ModelRegistro.objects.all()
        personas_serializer = PersonasSerializer(personas, many=True)
        return JsonResponse(personas_serializer.data, safe=False)

    elif request.method == 'POST':
        personas_data = JSONParser().parse(request)
        personas_serializer = PersonasSerializer(data=personas_data)
        if personas_serializer.is_valid():
             personas_serializer.save()
             return JsonResponse(personas_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


    elif request.method == 'PUT': 
        personas_data = JSONParser().parse(request) 
        personas_serializer = PersonasSerializer(personas, data=personas_data) 
        if personas_serializer.is_valid(): 
            personas_serializer.save() 
            return JsonResponse(personas_serializer.data) 
        return JsonResponse(personas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    elif request.method == 'DELETE':
            ModelRegistro.objects.all().delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)    
                

