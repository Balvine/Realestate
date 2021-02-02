from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(models.Model):
    User = models.ForeignKey(User,on-delete = models.CASCADE,related-name = 'user-profile')
    first_name= =models.name = models.CharField(max_length=length,  null=True)
    last-name = models.name = models.CharField(max_length=length,  null=True)
    
    
    
    
    
    class Post (models.Model):
         title = models.CharField(max_length = 50)
    content = models.TextField()
    User= models.ForeignKey(User,on_delete = models.CASCADE)
    