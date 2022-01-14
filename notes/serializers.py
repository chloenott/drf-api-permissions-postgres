from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'headline', 'details', 'datetime_created', 'datetime_updated', 'user']
        model = Note