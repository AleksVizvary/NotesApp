from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_note')
    else:
        form = NoteForm()


    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'add_note.html', {'form': form, 'notes': notes})
