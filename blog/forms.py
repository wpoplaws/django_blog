from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title',  'description', 'date_added', 'image', 'author', 'status']
