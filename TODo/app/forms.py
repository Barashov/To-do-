from django import forms


class AddForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название:')
    description = forms.CharField(widget=forms.Textarea, label='Описание:')
    
