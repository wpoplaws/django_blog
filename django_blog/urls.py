from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from blog import views
from blog.views import new_post, update_post, delete_post, post_list, post_detail, ask_question, question_confirm, \
    messages_list, delete_message
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog.feeds import LastestPostsFeed

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet, basename='name')
router.register(r'comments', views.CommentsViewSet)
from rest_framework.authtoken import views

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
                  path('rest', include(router.urls)),
                  path('feed/', LastestPostsFeed(), name='post_feed'),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('auth/', views.obtain_auth_token),
                  path('new_post/', new_post, name="new_post"),
                  path('question_confirm/', question_confirm, name="question_confirm"),
                  path('ask_question/', ask_question, name="ask_question"),
                  path('update_post/<int:id>/', update_post, name="update_post"),
                  path('delete_post/<int:id>/', delete_post, name="delete_post"),
                  path('delete_message/<int:id>/', delete_message, name="delete_message"),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path('', post_list, name='post_list'),
                  path('messages_list', messages_list, name='messages_list'),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
