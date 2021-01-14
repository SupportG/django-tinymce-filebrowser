from django.db import models
from tinymce.models import HTMLField


class testPosts(models.Model):
    title = models.CharField(max_length=200)
    exerpt = models.TextField(max_length=200)
    content = HTMLField()
