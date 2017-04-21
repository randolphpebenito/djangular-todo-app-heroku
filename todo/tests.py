from __future__ import unicode_literals
import json

from django.core.urlresolvers import reverse
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

class TodoListCreateViewTest(APITestCase):
    url = reverse('todo:todo-list-create')

    def setUp(self):
        pass

    def test_missing_blank_request(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)

    def test_title_char_exceeded(self):
        data = { 
            "title": "this title view exceeds 64 char Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.", 
            "note": "This is just a note" 
        }
        json_data = json.dumps(data)
        response = self.client.post(self.url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_todo(self):
        data = { 
            "title": "This is my todo", 
            "note": "This is just a note" 
        }
        json_data = json.dumps(data)
        response = self.client.post(self.url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_todo_return_must_be_list(self):
        Todo.objects.create(title="This is my todo", note="This is just a note")
        response = self.client.get(self.url)
        self.assertTrue(isinstance(json.loads(response.content), list))

    def test_validate_list_count(self):
        Todo.objects.bulk_create([
                Todo(title="This is my todo", note="This is just a note"),
                Todo(title="This is my todo2", note="This is just a note2")
            ])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 2)

class TodoRetrieveUpdateDeleteViewTest(APITestCase):

    def setUp(self):
        self.invalid_url = reverse('todo:todo-retrieve-update-delete', kwargs={'pk': 1000}) #Not existing pk

    def test_retrieve_invalid_pk(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_update_invalid_pk(self):
        response = self.client.put(self.invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_pk(self):
        response = self.client.put(self.invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_retrieve_successful(self):
        Todo.objects.create(title="This is my todo", note="This is just a note")

        url = reverse('todo:todo-retrieve-update-delete', kwargs={'pk': 1}) #Not existing pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEquals(response_data['id'], 1)

    def test_update_successful(self):
        a = Todo.objects.create(title="This is my todo", note="This is just a note")
        url = reverse('todo:todo-retrieve-update-delete', kwargs={'pk': a.pk}) #Not existing pk
        self.assertFalse(a.completed)
        
        json_data = json.dumps({ 'completed': True })
        response = self.client.patch(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        aa = Todo.objects.get(pk=a.pk)
        self.assertTrue(aa.completed)

    def test_delete_successful(self):
        a = Todo.objects.create(title="This is my todo", note="This is just a note")
        url = reverse('todo:todo-retrieve-update-delete', kwargs={'pk': a.pk}) #Not existing pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(pk=a.pk)
t
