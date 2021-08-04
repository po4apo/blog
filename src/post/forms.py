from django import forms

from .models import Coment


class ComentForm(forms.ModelForm):
    userName = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder":"Ваше имя"}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={"class": "form-control mb-3", "placeholder":"Добавьте свой коментарий", "rows":"3"}))

    class Meta:
        model = Coment
        fields = ('userName', 'body')
