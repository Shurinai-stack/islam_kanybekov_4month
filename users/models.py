from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    age = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name}'
