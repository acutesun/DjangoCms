from django.contrib import admin
from django.db import models
from django import forms

from .models import Comment, Article, Column, UserProfile, Author


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'pub_time', 'body', 'poll_num']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'profile')


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
            attrs={'rows': 41,
                   'cols': 100
                   })},
    }
    list_display = ('title', 'pub_time', 'poll_num')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Author, AuthorAdmin)