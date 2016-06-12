from django import forms
from django.forms import ModelForm
from .models import Post, Comment

__author__ = 'Artem Kraynev'


class WritePostForm(ModelForm):
    """
    Форма написания статьи
    """

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'contents_of_post',
        )


class EditPostForm(ModelForm):
    """
    Форма редактирования статьи
    """

    class Meta:
        model = Post
        fields = (
            'title',
            'redactor',
            'date_of_change',
            'contents_of_post',
        )


class CommentForm(ModelForm):
    parent = forms.CharField(
        widget=forms.HiddenInput(attrs={'class': 'parent'}),
        required=False
    )

    class Meta:
        model = Comment
        fields = (
            'post',
            'author',
            'email',
            'comment_text',
        )

