from django.contrib import admin

from .models import Comment, News


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
