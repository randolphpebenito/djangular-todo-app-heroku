from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Todo
from .serializers import TodoSerializer

class TodoSerializerTest(APITestCase):
    def setUp(self):
        pass

    def test_blank_fields(self):
        data = {}
        serializer = TodoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_missing_title_field(self):
        data = { "note": "This is just a note" }
        serializer = TodoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertRegexpMatches( str(serializer.errors), "title")
        self.assertRegexpMatches( str(serializer.errors), "This field is required")

    def test_title_char_exceeded(self):
        data = { 
            "title": "this title exceeds 64 char Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.", 
            "note": "This is just a note" 
        }
        serializer = TodoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertRegexpMatches( str(serializer.errors), "title")
        self.assertRegexpMatches( str(serializer.errors), "Ensure this field has no more than 64 characters.")

    def test_create_todo(self):
        data = { 
            "title": "This is my todo", 
            "note": "This is just a note" 
        }
        serializer = TodoSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        s = serializer.save()
        self.assertEquals(s.title, "This is my todo")

