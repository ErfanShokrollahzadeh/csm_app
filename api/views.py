from django.shortcuts import render
from . import models


def index(request):
    context = {
        'todos': models.Todo.objects.order_by('priority').all()
    }
    return render(request, 'index.html', context)
