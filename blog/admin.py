from django.contrib import admin
from .models import Post, Comments, Question


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date_added", "author", 'status']
    list_filter = ["date_added", 'status']
    search_fields = ["title", "description"]
    ordering = ['date_added', 'author', 'status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comments)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "comments","create_date"]
    list_filter = ["create_date", 'email']
    search_fields = ["email", "name"]
    ordering = ['create_date']
