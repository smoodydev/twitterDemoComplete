from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A single Blog post
    """
    user = models.ForeignKey(User, related_name="posts")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.user


class Likes(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="liked_by")
    user = models.ManyToManyField(User, related_name="likes")
    