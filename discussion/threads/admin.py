from django.contrib import admin
from .models import Thread, Comment, Likes, Dislikes, Profile, Category, WatchThread


class CommentInline(admin.TabularInline):  # adding an extra comment viewable option in our admin page
    model = Comment
    extra=0


class ThreadAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment)
# registerin the likes
admin.site.register(Likes)
# registering the dislieks
admin.site.register(Dislikes)
#the profile
admin.site.register(Profile)

admin.site.register(Category)

admin.site.register(WatchThread)