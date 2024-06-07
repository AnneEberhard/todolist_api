
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer
from django.core import serializers


from rest_framework.response import Response
from rest_framework import status

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request, *args, **kwargs):
        title = request.data.get('title', '')
        description = request.data.get('description', '')
        todo = Todo.objects.create(title=title, description=description, user=request.user)
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type='application/json')
