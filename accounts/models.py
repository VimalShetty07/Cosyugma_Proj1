from email.policy import default
import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,related_name = 'profile')
    phone_number = models.CharField(max_length=12)
    otp = models.CharField(max_length=100,null=True,blank=True)
    uid = models.UUIDField(default=uuid.uuid4)
    