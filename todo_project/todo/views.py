from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import TodoItem, Tag
from .serializers import TodoItemSerializer, TagSerializer

# Create your views here.

class TodoItemCreateAPIView(generics.CreateAPIView):
    """
    View to create a new todo item
    Endpoint: /api/todo/create/
    Allowed methods: POST
    Args: title, description, due_date, status, tags
    Additional: created_at is automatically set to current time
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def create(self, request, *args, **kwargs):
        """
        Override create method to handle tags
        """
        tags = request.data.pop('tags', [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        todo_item = TodoItem.objects.get(pk=serializer.data['id'])
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            todo_item.tags.add(tag_obj)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
    
class TodoItemListAPIView(generics.ListAPIView):
    """
    View to list all todo items
    Endpoint: /api/todo/list/
    Allowed methods: GET
    Args: None
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a todo item
    Endpoint: /api/todo/<int:pk>/
    Allowed methods: GET
    Args: id
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoUpdateAPIView(generics.UpdateAPIView):
    """
    View to update a todo item
    Endpoint: /api/todo/update/<int:pk>/
    Allowed methods: PUT
    Args: id, title, description, due_date, status, tags
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def update(self, request, *args, **kwargs):
        """
        Override update method to handle tags
        """
        tags = request.data.pop('tags', [])
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        todo_item = TodoItem.objects.get(pk=serializer.data['id'])
        todo_item.tags.clear()
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            todo_item.tags.add(tag_obj)
        return Response(serializer.data)


class TodoDeleteAPIView(generics.DestroyAPIView):
    """
    View to delete a todo item
    Endpoint: /api/todo/delete/<int:pk>/
    Allowed methods: DELETE
    Args: id
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoRetriveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a todo item
    Endpoint: /api/todo/<int:pk>/
    Allowed methods: GET, PUT, DELETE
    Args: id
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer