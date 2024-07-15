# todo/urls.py
from django.urls import path
from .views import ToDoListView, ToDoDetailView, ToDoCreateView, ToDoUpdateView, ToDoDeleteView

urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>/', ToDoDetailView.as_view(), name='todo_detail'),
    path('todo/new/', ToDoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/edit/', ToDoUpdateView.as_view(), name='todo_edit'),
    
    path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
]
