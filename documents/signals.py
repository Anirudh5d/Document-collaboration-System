from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Document
from .serializers import DocumentSerializer

CACHE_TTL = 60 * 15  # Cache timeout (15 minutes)

@receiver(post_save, sender=Document)
def update_cache(sender, instance, **kwargs):
    cache_key = f'document_{instance.id}'
    cache.set(cache_key, DocumentSerializer(instance).data, timeout=CACHE_TTL)
