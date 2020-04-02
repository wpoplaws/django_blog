from django.forms import ModelForm
from .models import Post, Comments, Question
from ckeditor.fields import RichTextFormField
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django.conf import settings


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
    captcha = ReCaptchaField(label="")
    class Meta:
        model = Question
        fields = ('name', 'email', 'phone_number', 'comments', )
        labels = {
            "name": "Imię i Nazwisko*",
            "comments": "Wiadomość*",
            "email": "Email*",
            "phone_number": "Numer telefonu",
            "captcha": " ",
        }
