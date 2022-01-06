from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    referrer_id = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.phone_number