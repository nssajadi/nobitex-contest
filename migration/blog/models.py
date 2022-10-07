from django.db import models
from django.contrib.auth import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
