from django.urls import path
from .views import TodoItemCreateAPIView, TodoItemListAPIView, TodoItemDetailAPIView, TodoUpdateAPIView, TodoDeleteAPIView, TodoRetriveUpdateDeleteAPIView

urlpatterns = [
    # Create a new todo item
    path('todo/create/', TodoItemCreateAPIView.as_view(), name='todo_create'),

    # List all todo items
    path('todo/list/', TodoItemListAPIView.as_view(), name='todo_list'),

    # Retrieve a specific todo item
    path('todo/<int:pk>/', TodoItemDetailAPIView.as_view(), name='todo_detail'),

    # Update a specific todo item
    path('todo/update/<int:pk>/', TodoUpdateAPIView.as_view(), name='todo_update'),

    # Delete a specific todo item
    path('todo/delete/<int:pk>/', TodoDeleteAPIView.as_view(), name='todo_delete'),

    # Comprehensive view to retrieve, update or delete a todo item
    path('retrive_update_delete/<int:pk>/', TodoRetriveUpdateDeleteAPIView.as_view(), name='todo_manage')
]