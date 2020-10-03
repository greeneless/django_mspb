from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ForumPost(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# parent model
class Forum(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    # email = models.CharField(max_length=256, null=True)
    topic = models.CharField(max_length=256)
    description = models.CharField(max_length=2048, blank=True)
    # link = models.CharField(max_length=256, null=True)
    # date_posted = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.topic)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=2048)

    def __str__(self):
        return str(self.forum)