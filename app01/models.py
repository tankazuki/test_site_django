from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Memo(models.Model):
    title = models.CharField(null=False, max_length=50)
    memo = models.TextField(null=False, max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





