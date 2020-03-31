from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from blog import views
from blog.views import new_post, update_post, delete_post, post_list
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet, basename='name')
router.register(r'comments', views.CommentsViewSet)
from rest_framework.authtoken import views

urlpatterns = [
    path('rest', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('auth/', views.obtain_auth_token),
    path('new_post/', new_post, name="new_post"),
    path('update_post/<int:id>/', update_post, name="update_post"),
    path('delete_post/<int:id>/', delete_post, name="delete_post"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', post_list, name='post_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
