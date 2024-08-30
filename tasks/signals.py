from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Task
from .serializers import TaskSerializer

CACHE_TTL = 60 * 15  # Cache timeout (15 minutes)

@receiver(post_save, sender=Task)
def update_task_cache(sender, instance, **kwargs):
    cache_key = f'task_{instance.id}'
    cache.set(cache_key, TaskSerializer(instance).data, timeout=CACHE_TTL)
