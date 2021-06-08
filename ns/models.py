from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
from django.db.models.signals import *
from django.db.models.signals import post_save
class oldsell(models.Model):
    name = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    bidstart = models.IntegerField()
    picture = models.ImageField(upload_to='oldsell/' , blank=True)     
    seller= models.CharField(max_length=225)
    date=models.CharField(max_length=50)
class newsell(models.Model):
    name = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='newsell/' , blank=True)     
    quantity= models.PositiveIntegerField()
    seller= models.CharField(max_length=225)
    date=models.CharField(max_length=50)
class SignUp(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=50)
    def __str__(self):  # __str__
        return (self.user.username)
#def create_profile(sender, **kwargs):
#   if kwargs ['created']:
#        user = kwargs["instance"]
#        reg=UserProfile(user=user,usernames=user.username,phoneno="none",address="none",gender="other")
#        reg.save()
#        user_profile= UserProfile.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile, sender=User, dispatch_uid="users-profilecreation-signal")
class Feedback(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=200)
    msg=models.CharField(max_length=500)

    