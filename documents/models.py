from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from users.models import Base
User = get_user_model()

class Document(Base):
    title = models.CharField(max_length=255)
    content = models.TextField()
    collaborators = models.ManyToManyField(User, related_name='documents')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_documents')
    allocated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allocated_documents', null=True, blank=True)

    def __str__(self):
        return self.title
