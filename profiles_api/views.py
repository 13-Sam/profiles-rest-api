from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from . serializers import UserProfileSerializer, ProfileFeedItemSerializer
from . models import UserProfile, ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
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
    

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset = [
            'hello1',
            'hello2',
            'hello3'
        ]
        return Response({'message':'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'HELLO {name}!'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})
    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')
    

class UserLoginApiView(ObtainAuthToken):
    '''Handle Creating User Authentication'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (IsAuthenticated,
                          permissions.UpdateOwnStatus)
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)