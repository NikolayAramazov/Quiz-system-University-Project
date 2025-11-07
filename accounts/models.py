from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(default='profile_pictures/default_profile_pic.png', upload_to='profile_pictures/')
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
