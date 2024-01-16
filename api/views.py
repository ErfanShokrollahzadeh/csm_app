from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new
from . import models


def index(request):
    context = {
        'todos': models.Todo.objects.order_by('priority').all()
    }
    return render(request, 'index.html', context)


@api_view(['GET'])
def todo_json(request: Request):
    todos = list(models.Todo.objects.order_by(
        'priority').all().values('title', 'is_done'))

    return Response({'todos': todos}, status.HTTP_200_OK)
