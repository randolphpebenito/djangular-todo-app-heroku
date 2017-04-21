# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView

from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
            Sort Todo List by its latest date (updated)
        """
        return Todo.objects.order_by('-updated_at')
