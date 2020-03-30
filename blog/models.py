from datetime import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Comments(models.Model):
    com_author = models.CharField(max_length=200)
    com_text = models.TextField()
    com_created_date = models.DateTimeField(default=datetime.now, blank=True)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', "Published"),
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=40, unique_for_date='date_added', blank=True)
    description = models.TextField(default="")
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to="Images", blank=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

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
