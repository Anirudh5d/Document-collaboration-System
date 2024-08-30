from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer, CollaboratorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from .utilities import get_document_from_cache, update_document
from django.core.cache import cache


CACHE_TTL = 60 * 15  # 15 minutes

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.filter(status=1)
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.filter(status=1)
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = f'document_{instance.id}'
        cache.delete(cache_key)
        cache.set(cache_key, DocumentSerializer(instance).data, timeout=CACHE_TTL)
        return instance

    def perform_destroy(self, instance):
        cache_key = f'document_{instance.id}'
        cache.delete(cache_key)
        instance.status = 0
        instance.save()

class DocumentDetailView(generics.RetrieveAPIView):
    queryset = Document.objects.filter(status=1)
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        document_id = kwargs.get('pk')
        document = get_document_from_cache(document_id)
        if not document:
            return Response({'error': 'Document not found'}, status=404)

        response_data = {
            "source": document.get('source'),
            "document": document.get('document'),
            "cache_time": document.get('cache_time'),
            "db_time": document.get('db_time')
        }

        return Response(response_data)
    
class CollaboratorUpdateView(generics.UpdateAPIView):
    queryset = Document.objects.filter(status=1)
    serializer_class = CollaboratorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admins can modify collaborators.")
        return super().get_queryset()

@api_view(['PUT'])
def update_document_view(request, document_id):
    data = request.data
    try:
        document = update_document(document_id, data)
        return Response({"message": "Document updated successfully"}, status=status.HTTP_200_OK)
    except Document.DoesNotExist:
        return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
