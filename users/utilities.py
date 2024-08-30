from django.core.cache import cache
from .models import UserProfile, UserRole
from .serializers import UserProfileSerializer, UserRoleSerializer
import time

CACHE_TTL = 60 * 15  # 15 minutes

def get_userprofile_from_cache(userprofile_id):
    cache_key = f'userprofile_{userprofile_id}'
    userprofile = cache.get(cache_key)

    if not userprofile:
        try:
            userprofile = UserProfile.objects.get(id=userprofile_id)
            serializer = UserProfileSerializer(userprofile)
            userprofile_data = serializer.data
            cache.set(cache_key, userprofile_data, timeout=CACHE_TTL)
        except UserProfile.DoesNotExist:
            return None

    response = {
        "source": "cache",
        "cache_time": time.time(),
        "db_time": userprofile.updated_at.timestamp(),
        "userprofile": userprofile
    }
    return response

def get_userrole_from_cache(userrole_id):
    cache_key = f'userrole_{userrole_id}'
    userrole = cache.get(cache_key)

    if not userrole:
        try:
            userrole = UserRole.objects.get(id=userrole_id)
            serializer = UserRoleSerializer(userrole)
            userrole_data = serializer.data
            cache.set(cache_key, userrole_data, timeout=CACHE_TTL)
        except UserRole.DoesNotExist:
            return None

    response = {
        "source": "cache",
        "cache_time": time.time(),
        "db_time": userrole.updated_at.timestamp(),
        "userrole": userrole
    }
    return response
