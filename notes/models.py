from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Note(models.Model):
    headline = models.CharField(max_length=64)
    details = models.TextField(default="")
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    