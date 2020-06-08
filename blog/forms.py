from .models import Comment
from django.forms import ModelForm
from django import forms


class CommentForm(forms.ModelForm):
    comment=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Text goes here!!','rows':'3'}))
    class Meta:
        model=Comment
        fields=('comment',)
    