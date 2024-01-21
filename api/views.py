from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from .models import Todo
from .serializer import TodoSerializer


@api_view(['GET'])
def all_todos(request: Request):
    todos = Todo.objects.order_by('priority').all()
    todos_serializer = TodoSerializer(todos, many=True)
    return Response(todos_serializer.data, status.HTTP_200_OK)
