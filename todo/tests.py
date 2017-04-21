from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Todo
from .serializers import TodoSerializer

class TodoSerializerTest(APITestCase):
    def setUp(self):
        pass

