from django.shortcuts import render
from notes.models import Note

def test_view(request):
    notes = Note.objects.first()
    return render(request, 'test.html', {'note': notes})