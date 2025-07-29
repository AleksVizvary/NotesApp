from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title:'}),
            'content': forms.TextInput(attrs={'placeholder': 'Content'}),
            'tags': forms.TextInput(attrs={'placeholder': 'tags:'})
        }
