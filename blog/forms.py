from django.forms import ModelForm
from .models import Post, Comments, Question, Signup
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
        fields = ['title', 'description', 'date_added', 'tags', 'image', 'author', 'status']
        widgets = {
            'content': RichTextFormField()}

        labels = {
            "title": "Tytuł",
            "description": "Opis",
            "date_added": "Data dodania",
            "image": "Zdjęcie",
            "author": "Autor",
            "status": "Status",
            "tags": "Tagi",
        }
        help_texts = {'tags': "Rozdzielona przecinkami lista tagów", }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'email', 'text',)
        labels = {
            "text": "Treść",
            "email": "Email",
            "author": "Autor",

        }


class EmailPostForm(ModelForm):
    captcha = ReCaptchaField(label="")

    class Meta:
        model = Question
        fields = ('name', 'email', 'phone_number', 'comments',)
        labels = {
            "name": "Imię i Nazwisko*",
            "comments": "Wiadomość*",
            "email": "Email*",
            "phone_number": "Numer telefonu",
        }


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Wpisz swój adres e-mail ",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email',)
