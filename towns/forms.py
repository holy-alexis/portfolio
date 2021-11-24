from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class search_form:
        model = Post
        fields = ('name',)
