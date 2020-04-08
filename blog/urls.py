from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .feeds import LastestPostsFeed

app_name = 'blog'

urlpatterns = [
                  path('', views.post_list, name='post_list'),
                  path('<int:year>/<int:month>/<int:day>/<slug:post>/',
                       views.post_detail,
                       name="post_detail"),
                  path('tag/<slug:tag_slug>/',
                       views.post_list, name='post_list_by_tag'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
