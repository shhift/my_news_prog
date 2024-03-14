from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Reporter(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    publish = models.DateTimeField(default=timezone.now())
    headline = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_articles")

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]

    def __str__(self):
        return self.headline
