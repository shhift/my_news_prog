from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    publish = models.DateField(default=timezone.now)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_articles"
    )

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.headline
