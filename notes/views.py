from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
