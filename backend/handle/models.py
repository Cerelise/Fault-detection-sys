from django.db import models

# Create your models here.


class TrainsUpload(models.Model):
    train = models.FileField(upload_to='trains/')


class TestsUpload(models.Model):
    test = models.FileField(upload_to='tests/')

# class Rate(models.Model):
#     text = models.TextField(blank=True,null=True)
#     rating = models.IntegerField(default=0)
