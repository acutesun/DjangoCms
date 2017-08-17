from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProfile(AbstractUser):
    profile = models.CharField(max_length=256, default='', verbose_name='简介')

    def __str__(self):
        return '<UserProfile_{0}>'.format(self.username)


class Column(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类名', unique=True)
    intro = models.TextField()

    def __str__(self):
        return '<Column_{0}'.format(self.name)

    class Meta:
        verbose_name = 'column'
        verbose_name_plural = verbose_name
        ordering = ['name']


class ArticleManager(models.Manager):
    def query_by_column(self, column_id):
        query = self.get_queryset().filter(column_id=column_id)

    def query_by_user(self, user_id):
        user = User.objects.get(id=user_id)
        article_list = user.article_set.all()
        return article_list

    def query_by_polls(self):
        query = self.get_queryset().order_by('poll_num')
        return query

    def query_by_time(self):
        query = self.get_queryset().order_by('-pub_time')
        return query

    def query_by_keyword(self, keyword):
        query = self.get_queryset().filter(title__contains=keyword)
        return query


class Article(models.Model):
    objects = ArticleManager()

    title = models.CharField(max_length=256)
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True, editable=True)
    mod_time = models.DateTimeField(auto_now=True, null=True)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    keep_num = models.IntegerField(default=0)

    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='belong to')
    author = models.ForeignKey('Author')
    user = models.ManyToManyField(UserProfile, blank=True)

    def __str__(self):
        return '<Article_{0}'.format(self.title)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    body = models.CharField(max_length=600)
    pub_time = models.DateTimeField(auto_now_add=True, editable=True)
    poll_num = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article)

    def __str__(self):
        return '<Comment_{0}'.format(self.body[:20])


class Author(models.Model):
    name = models.CharField(max_length=256)
    profile = models.CharField('profile', default='', max_length=256)
    password = models.CharField('password', max_length=256)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name


class Poll(models.Model):
    user = models.ForeignKey(UserProfile, null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)