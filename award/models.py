from django.contrib.auth.models import User
from django.db import models


class Award(models.Model):
    company = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='award_photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='awards')
