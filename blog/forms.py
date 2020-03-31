from django.forms import ModelForm
from .models import Post
from ckeditor.fields import RichTextFormField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title',  'description', 'date_added', 'image', 'author', 'status']
        widgets = {
            'content': RichTextFormField()}
