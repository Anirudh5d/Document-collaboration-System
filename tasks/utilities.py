from django.core.cache import cache
from .models import Task
from .serializers import TaskSerializer
import time

CACHE_TTL = 60 * 15  # 15 minutes

def get_task_from_cache(task_id):
    cache_key = f'task_{task_id}'

    # Measure time taken to fetch from the cache
    start_time_cache = time.time()
    task_data = cache.get(cache_key)
    cache_time = time.time() - start_time_cache
    source = "cache"

    if not task_data:
        try:
            # Measure time taken to fetch from the database
            start_time_db = time.time()
            task = Task.objects.get(id=task_id)
            db_time = time.time() - start_time_db

            serializer = TaskSerializer(task)
            task_data = serializer.data

            # Store in cache if DB fetch is faster
            if db_time < cache_time:
                cache.set(cache_key, task_data, timeout=CACHE_TTL)
                source = "database"
            else:
                source = "cache"

        except Task.DoesNotExist:
            return None

    return {
        "source": source,
        "cache_time": cache_time,
        "db_time": task_data['updated_at'] if task_data else None,
        "task": task_data
    }
