from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    location=models.CharField(max_length=250, blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    avatar=models.ImageField(upload_to='profilepics/', blank=True, null=True, default='',)

    def __str__(self):
        return self.user