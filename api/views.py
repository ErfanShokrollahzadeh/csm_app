from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from rest_framework.views import APIView  # new *
from .models import Todo
from .serializer import TodoSerializer


class TodosListApiView(APIView):
    def get(self, request=Request):
        todos = Todo.objects.order_by('priority').all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requst=Request):
        serializer = TodoSerializer(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class TodosDetailApiView(APIView):
    def get(self, request=Request, pk=None):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request=Request, pk=None):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request=Request, pk=None):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
