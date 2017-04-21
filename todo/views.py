# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Todo
from .serializers import TodoSerializer

def index(request):
    """
        Main Page (Single Page Application)
    """
    return render(request, "index.html", {})

class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
            Sort Todo List by its latest date (updated)
        """
        return Todo.objects.order_by('-updated_at')

class TodoRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
