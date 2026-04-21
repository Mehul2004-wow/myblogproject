from django.db import models
# Create your models here.
class Contact_us(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.CharField()
    comment=models.CharField()

class Registration(models.Model):
    Name=models.CharField(max_length=100,blank=False)
    User_name=models.CharField(max_length=10,blank=False)
    MobileNo=models.IntegerField(blank=False)
    Password=models.CharField(blank=False)
    Re_Password=models.CharField(blank=False)

class Post(models.Model):
    id = models.AutoField(primary_key=1)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Category(models.Model):
    id = models.AutoField(primary_key=1)
    name = models.CharField(max_length=100)
    description = models.TextField()