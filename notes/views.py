from rest_framework import generics
from .models import Notes
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):   # CRUD
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    