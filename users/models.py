from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pub = models.BooleanField('Разрешение на публикацию', default=True)

    def __str__(self) -> str:
        return self.user.username
