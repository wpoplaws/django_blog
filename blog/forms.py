from django.forms import ModelForm
from .models import Post, Comments, Question
from ckeditor.fields import RichTextFormField
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'date_added', 'image', 'author', 'status']
        widgets = {
            'content': RichTextFormField()}

        labels = {
            "title": "Tytuł",
            "description": "Opis",
            "date_added": "Data dodania",
            "image": "Zdjęcie",
            "author": "Autor",
            "status": "Status",
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text',)


class EmailPostForm(ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'comments',)
        labels = {
            "name": "Imię",
            "comments": "Pytanie",
        }