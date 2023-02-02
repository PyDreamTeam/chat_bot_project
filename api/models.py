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
    REQUIRED_FIELDS = ['email', 'password']
     
        
    def __str__(self):
        return self.email      
        
        
    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name    
     
        
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
        
     