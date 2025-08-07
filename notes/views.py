from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import NoteForm
from .models import Note

def add_note(request):
    show_done = request.GET.get("show_done") == "1"
    show_all = request.GET.get("show_all") == "1"
    query = request.GET.get('search', '')

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_note')
    else:
        form = NoteForm()

    notes = Note.objects.all()

    if not show_all:
        if show_done:
            notes = notes.filter(done=True)
        else:
            notes = notes.filter(done=False)

    if query:
        notes = Note.objects.all()
        notes = notes.filter(title__icontains=query)


    return render(request, 'add_note.html', {
        'form': form,
        'notes': notes,
        'show_done': show_done,
        'query': query,
    })

def mark_done(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.done = not note.done
    note.save()

    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return redirect(reverse('add_note'))