from django.conf.urls import url

from .views import TodoListCreateView

app_name = 'todo'
urlpatterns = [
    url(r'^$', TodoListCreateView.as_view(), name='todo-list-create'),
]


