from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class notes(models.Model):
    description = models.TextField()
    date = models.DateField(
        null=True,
        default=datetime.now()
    )
    user = models.ForeignKey(
        User,
        default=User,
        on_delete=models.CASCADE,
        null=True)
    parent = models.TextField(default="Talent is Never Enough")
    title = models.TextField(default="Exercise")

