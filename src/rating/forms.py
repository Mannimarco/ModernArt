from django import forms

from rating.models import Vote


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ()
