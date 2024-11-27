from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    is_done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
