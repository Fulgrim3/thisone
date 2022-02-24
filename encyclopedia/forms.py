from django import forms

from .models import Entry
from .models import Edit

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'title',
            'Body'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleField'}),
            'Body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        fields = [
            'Body'
        ]
        widgets = {
            'Body': forms.Textarea(attrs={'class': 'form-control'})
        }