from django.utils import timezone

from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now() + timezone.timedelta(days=7)
    )
    is_complete = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["is_complete", "-datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
