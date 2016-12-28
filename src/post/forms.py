from django import forms

from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'encoded_image')
        widgets = {'encoded_image': forms.HiddenInput()}


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'encoded_image')
        widgets = {'encoded_image': forms.HiddenInput()}


class SearchForm(forms.Form):
    text = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Search',
        'style': 'color: #FFFFFF;',
    }))
    order = forms.ChoiceField(choices=(
        ('-created_date', 'Date desc'),
        ('created_date', 'Date asc'),
        ('author', 'Author'),
    ))
    # direction = forms.ChoiceField(choices=(('ascending', 'Ascending'), ('descending', 'Descending')))
