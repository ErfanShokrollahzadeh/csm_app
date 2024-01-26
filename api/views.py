from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from .models import Todo
from .serializer import TodoSerializer


@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(requst: Request, pk: int):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if requst.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif requst.method == 'PUT':
        serializer = TodoSerializer(todo, data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
    elif requst.method == 'DELETE':
        todo.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
