from django.conf.urls import url

from .views import TodoListCreateView, TodoRetrieveUpdateDeleteView

app_name = 'todo'
urlpatterns = [
    url(r'^$', TodoListCreateView.as_view(), name='todo-list-create'),
    url(r'^(?P<pk>[0-9]+)$', TodoRetrieveUpdateDeleteView.as_view(), name='todo-retrieve-update-delete'),
]


