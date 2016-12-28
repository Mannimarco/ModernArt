from django import forms
from django.views.generic import DetailView

from .models import Comment


class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

