from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', "Published"),
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=40, unique_for_date='date_added', blank=True)
    description = RichTextUploadingField(default="")
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to="Images", blank=True, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(blank=True, )

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.date_added.year,
                             self.date_added.month,
                             self.date_added.day,
                             self.slug])


class Comments(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments', default=" ")
    author = models.CharField(max_length=200)
    email = models.EmailField(default="")
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_date',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Question(models.Model):
    name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    comments = models.TextField(max_length=2000, blank=False)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    phone_number = models.CharField(max_length=12, blank=True, default="")


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
