import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def time_passed(self):
        today = date.today()
        difference = today - self.created_at
        return difference.days