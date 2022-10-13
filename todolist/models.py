from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.datetime.now)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)