from email.policy import default
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    location     = models.CharField(max_length=250, blank=True, null=True)
    bio          = models.TextField(blank=True, null=True)
    avatar_url   = models.ImageField(
                        upload_to='profilepics/', 
                        blank=True, null=True
                    )

    def __str__(self):
        return str(self.user)