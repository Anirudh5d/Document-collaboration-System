from django.core.cache import cache
from .models import Document
from .serializers import DocumentSerializer
import time

CACHE_TTL = 60 * 15  # 15 minutes

def get_document_from_cache(document_id):
    cache_key = f'document_{document_id}'

    # Measure time taken to fetch from the cache
    start_time_cache = time.time()
    document_data = cache.get(cache_key)
    cache_time = time.time() - start_time_cache
    source = "cache"

    if not document_data:
        try:
            # Measure time taken to fetch from the database
            start_time_db = time.time()
            document = Document.objects.get(id=document_id)
            db_time = time.time() - start_time_db

            serializer = DocumentSerializer(document)
            document_data = serializer.data

            # Store in cache if DB fetch is faster
            if db_time < cache_time:
                cache.set(cache_key, document_data, timeout=CACHE_TTL)
                source = "database"
            else:
                source = "cache"

        except Document.DoesNotExist:
            return None

    return {
        "source": source,
        "cache_time": cache_time,
        "db_time": document_data['updated_at'] if document_data else None,
        "document": document_data
    }

def update_document(document_id, data):
    document = Document.objects.get(id=document_id)
    document.title = data['title']
    document.content = data['content']
    document.save()

    cache_key = f'document_{document_id}'
    cache.delete(cache_key)
    cache.set(cache_key, DocumentSerializer(document).data, timeout=CACHE_TTL)

    return document
