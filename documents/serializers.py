from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['collaborators']

    def validate(self, data):
        request = self.context.get('request')
        if not request.user.is_staff:
            raise serializers.ValidationError("Only admins can add or remove collaborators.")
        return data
