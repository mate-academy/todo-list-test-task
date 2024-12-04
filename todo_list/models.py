from datetime import datetime

from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    is_done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
