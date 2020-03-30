from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required
from .models import Post, Comments
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.serializers import UserSerializer, GroupSerializer, PostSerializer, CommentsSerializer
from .forms import PostForm


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)


def post_list(request):
    posty = Post.published.all()
    return render(request, 'blog/post_list.html', {"posty": posty})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             date_added__year=year,
                             date_added__month=month,
                             date_added__day=day)
    return render(request, 'blog/post_detail.html',
                  {'post': post})

@login_required
def new_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'blog/post_form.html', {"form": form})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'blog/post_form.html', {"form": form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('http://127.0.0.1:8000/')

    return render(request, 'blog/confirm.html', {"post": post})


class CommentsViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all().order_by('com_created_date')
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication,)
