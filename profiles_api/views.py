from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


# Create your views here.
class HelloAPIView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'api is good',
            'api is sufficient',
            'api is better',
            'api is best',
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})
    def post(self, request):
        '''Create a Hello msg with name'''
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')  
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        return Response({'method':'Delete'})