from django.contrib import admin
from .models import Comment, Blog, Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
