from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.
class User(AbstractUser):
    Gender = {'male':'male', 'female':'female', 'other':'other'}
    Role = {'manager':'manager', 'developer':'developer', 'team_leader':'team_leader'}

    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True,
                                    validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    gender = models.CharField(max_length=20, choices=Gender, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    pincode = models.BigIntegerField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    contact = models.BigIntegerField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=Role)
    company = models.CharField(max_length=20, blank=True, null=True)
