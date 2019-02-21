import uuid
from django.db import models
from django.contrib.auth.models import User


class ArchivePost(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    post_content = models.TextField()
    post_summary = models.TextField()
    post_image_alt_text = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        ArchiveYear.objects.create(year=self.year, post_id=self.post_id)
        super().save(*args, **kwargs)  

    def delete(self, *args, **kwargs):
        ArchiveYear.objects.filter(year=self.year, post_id=self.post_id).delete()
        super().delete(*args, **kwargs)
            

class ArchiveYear(models.Model):
    year = models.IntegerField()
    post_id = models.UUIDField(editable=False)