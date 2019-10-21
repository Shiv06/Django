from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    top_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    webpageName=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)

# class Register(models.Model):
#     name=models.CharField(max_length=500)
#     email=models.EmailField()
#     confirm_email=models.EmailField()
#     password=models.CharField(max_length=50)
#     confirm_password=models.CharField(max_length=50)
#     comments=models.CharField(max_length=5000)
#
#     def __str__(self):
#         return self.name

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
