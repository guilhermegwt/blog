from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()

    def __str__(self) -> str:
        return self.title