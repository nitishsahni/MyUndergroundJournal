from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=70)
    entry = models.TextField(max_length=10000)

    def __str__(self):
        return self.user.__str__() + ' | ' + self.title
