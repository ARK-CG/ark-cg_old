from django.db import models
from django.utils import timezone

# Create your models here.

class Gallery(models.Model):
    """作品のモデル"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey()

class Category(models.Model):
    """カテゴリー
    Galary(CG,イラスト,サービス)
    News,Blog"""
    name = models.CharField(max_length=256)

class Activity(models.Model):
    """アクティビティ"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey()