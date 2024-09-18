from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(to='Category', through='PostCategory')

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.category

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=2000)
    rating = models.IntegerField(default=0)
