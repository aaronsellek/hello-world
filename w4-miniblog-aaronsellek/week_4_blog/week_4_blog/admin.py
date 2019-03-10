from django.contrib import admin
from blog.models import Blogger, Topic, BlogPost

class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','bio')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'blogger', 'display_topic', 'post_date')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Topic)
admin.site.register(Blogger, BloggerAdmin)