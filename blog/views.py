from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required
from .models import Post, Comments, Question
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.serializers import UserSerializer, GroupSerializer, PostSerializer, CommentsSerializer
from .forms import PostForm, CommentForm, EmailPostForm
from django.core.paginator import Paginator


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
    al_posts = Post.published.all()
    paginator = Paginator(al_posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/post_list.html', {"posts": posts})


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
        return redirect('post_list')

    return render(request, 'blog/confirm.html', {"post": post})


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('com_created_date')
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication,)


def ask_question(request):
    question = EmailPostForm(request.POST or None, request.FILES or None)

    if question.is_valid():
        question.save()
        return redirect('question_confirm')

    return render(request, 'blog/ask_question.html', {"question": question})


def question_confirm(request):

    return render(request, 'blog/question_confirm.html', )


class Messages(object):
    pass


def messages_list(request):
    al_messages = Question.objects.all()
    paginator = Paginator(al_messages ,3)
    page = request.GET.get('page')
    messages = paginator.get_page(page)

    return render(request, 'blog/messages.html', {"messages": messages})


@login_required
def delete_message(request, id):
    message = get_object_or_404(Question, pk=id)
    form = EmailPostForm(request.POST or None, request.FILES or None, instance=message)

    if request.method == 'POST':
        message.delete()
        return redirect('messages_list')

    return render(request, 'blog/message_confirm.html', {"message": message})


