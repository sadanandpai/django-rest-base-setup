from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from portal.serializers import UserSerializer, FishSerializer
from portal.models import Fish as FishModel


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

@api_view(['GET', 'POST'])
def fish_list(request):
    """
    List all code snippets, or create a new fish.
    """
    context = {'request': request}
    if request.method == 'GET':
        fishes = FishModel.objects.all()
        serializer = FishSerializer(fishes, context=context, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fish_detail(request, pk):
    """
    Retrieve, update or delete a code fish.
    """
    # context = {'request': request}
    try:
        fishes = FishModel.objects.get(pk=pk)
    except FishModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FishSerializer(fishes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FishSerializer(fishes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fishes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def signin(request, format=None):
    return JsonResponse({'data': 'signin method is called'}, status=200)

def signup(request, format=None):
    return JsonResponse({'data': 'signup method is called'}, status=200)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    return JsonResponse({'data': 'Authentication successful'}, status=200)