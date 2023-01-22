from django import forms

from .models import Post


class NewPostOrUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status']
















