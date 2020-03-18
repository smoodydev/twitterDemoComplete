from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    bio = models.CharField(max_length=180, blank=False)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    followed = models.ForeignKey(User, related_name="followedBy")
    follower = models.ForeignKey(User, related_name="follows")