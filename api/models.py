from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE = [
        ('USER', "User"),
        ('ADMIN', "Admin"),
        ('MANAGER', "Manager"),
    ]

    user_role = models.CharField(max_length=10, choices=USER_ROLE, default='USER') 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
     
        
    def __str__(self):
        return self.email            
          
        
     