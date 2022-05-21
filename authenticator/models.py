from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
  owner = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(unique=True, null=True)
  bio = models.TextField(null=True)

  avatar = models.ImageField(null=True, default="avatar.svg")

  def __str__(self):
    return str(self.owner)
