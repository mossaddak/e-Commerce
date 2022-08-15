from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomeUserManager




#account type 
class Account_type(models.Model):
    account = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.account





class User(AbstractUser):


    email = models.EmailField( max_length=150,unique=True,error_messages={"unique":"The email must be unique."})
    
    profile_image = models.ImageField(null = True,blank = True,upload_to = "2_profile_image")
    phone_number = models.CharField(max_length=250, null=True, blank=True)

    account_type = models.CharField(max_length=250, blank=True, null=True)

    REQUIRES_FIELDS = ["email"]

    objects = CustomeUserManager()

    StoreBanner = models.ImageField(null = True,blank = True,upload_to = "3_store_banner")

    followers = models.ManyToManyField("Follow")

    Address = models.TextField(null=True,blank=True)

    

    def __str__(self):
        return str(self.pk) + "." + self.username

    
    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url

        except:
            url = ""
        return url

    def get_StoreBanner(self):
        url = ""
        try:
            url = self.StoreBanner.url

        except:
            url = ""
        return url

class Follow(models.Model):
    followed = models.ForeignKey(User, related_name='users_followers', on_delete=models.CASCADE)
    followed_by = models.ForeignKey(User, related_name='user_follows', on_delete=models.CASCADE)
    muted = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return   str(self.pk) + "." + f"{self.followed_by.username} started following { self.followed.username }" 

class Address(models.Model):
    User = models.ForeignKey(User, related_name="AddresRelatedName", on_delete=models.CASCADE, blank=True, null=True)
    Home = models.CharField(max_length=250, blank=True, null=True)
    Area = models.CharField(max_length=250, blank=True, null=True)
    PostOffice = models.CharField(max_length=250, blank=True, null=True)
    Upzilla = models.CharField(max_length=250, blank=True, null=True)
    Zilla = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}.{self.User}({self.Zilla})'




    