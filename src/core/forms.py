from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
