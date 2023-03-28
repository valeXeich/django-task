from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram_user_id = models.IntegerField(blank=True, null=True)
    telegram_photo = models.URLField(blank=True, null=True)
