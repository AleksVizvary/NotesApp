from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def add_note(request):
    show_done = request.GET.get("show_done") == "1"
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_note')
    else:
        form = NoteForm()

    if request.GET.get("show_done") == "1":
        notes = Note.objects.filter(done=True).order_by('-created_at')
    else:
        notes = Note.objects.filter(done=False).order_by('-created_at')

    return render(request, 'add_note.html', {
        'form': form,
        'notes': notes,
        'show_done': show_done,
    })


def mark_done(request, note_id):
    note = Note.objects.get(id=note_id)
    note.done = True
    note.save()
    next_url = request.GET.get('next', 'add_note')
    return redirect(next_url)
