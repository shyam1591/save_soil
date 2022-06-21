from django.db import models

# Create your models here.

class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255, default='SaveSoilCampaign')
    author = models.TextField(default="Shyam Mistry")
    status = models.TextField(default="draft")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

