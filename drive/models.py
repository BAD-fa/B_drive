from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    uploaded_size = models.IntegerField()


class File(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='files/')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)


