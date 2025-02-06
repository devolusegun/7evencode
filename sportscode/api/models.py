from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    pass

#BetCodes Model
class BettingCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_code = models.CharField(max_length=255)
    converted_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.user.username}: {self.original_code} -> {self.converted_code}"
    
#Messages Model
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
    
#Location Model
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user.username}: ({self.latitude}, {self.longitude})"
