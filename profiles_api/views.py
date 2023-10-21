from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    '''Test API View'''
    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'api is good',
            'api is sufficient',
            'api is better',
            'api is best',
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})