from django.urls import path
from .views import DocumentListCreateView, DocumentRetrieveUpdateDestroyView, CollaboratorUpdateView, DocumentDetailView, update_document_view

urlpatterns = [
    path('api/documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('api/documents/<int:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-detail'),
    path('api/documents/detail/<int:pk>/', DocumentDetailView.as_view(), name='document-detail-view'),
    path('api/documents/<int:pk>/collaborators/', CollaboratorUpdateView.as_view(), name='collaborator-update'),
    path('api/documents/<int:document_id>/update/', update_document_view, name='document-update'),
]
