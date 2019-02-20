from django.db import models
from django.contrib.auth.models import User


class ArchivePost(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    post_content = models.TextField()
    post_summary = models.TextField()
    post_image_alt_text = models.TextField()

    def __str__(self):
        return self.title