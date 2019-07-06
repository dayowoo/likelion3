from django.db import models

# Create your models here.
class Diary(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=30)
    image=models.ImageField(upload_to="image/",blank=True)
    time=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="image/",blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    

class HashTag(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)