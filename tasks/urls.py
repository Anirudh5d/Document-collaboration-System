from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskDetailView

urlpatterns = [
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('api/task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail-view'),
]
