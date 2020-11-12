from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Support(models.Model):
    agent_guid = models.CharField(max_length=256)
    summary = models.TextField()
    severity = models.CharField(max_length=256)
    scope = models.CharField(max_length=256)
