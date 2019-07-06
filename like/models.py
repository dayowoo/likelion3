from django.db import models
from django.contrib.auth.models import User
from diary.models import Diary

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)