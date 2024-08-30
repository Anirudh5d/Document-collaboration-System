from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utilities import get_task_from_cache
from django.core.cache import cache


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.filter(status=1)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.all()


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = f'task_{instance.id}'
        cache.delete(cache_key)
        cache.set(cache_key, TaskSerializer(instance).data)

    def perform_destroy(self, instance):
        cache_key = f'task_{instance.id}'
        cache.delete(cache_key)
        instance.status = 0
        instance.save()

    def perform_create(self, serializer):
        instance = serializer.save()
        cache_key = f'task_{instance.id}'
        cache.set(cache_key, TaskSerializer(instance).data)


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.filter(status=1)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        task_id = kwargs.get("pk")
        task = get_task_from_cache(task_id)
        if not task:
            return Response({'error': 'Task not found'}, status=404)

        response_data = {
            "source": task.get('source'),
            "cache_time": task.get('cache_time'),
            "db_time": task.get('db_time'),
            "task": task.get('task')
        }

        return Response(response_data)
