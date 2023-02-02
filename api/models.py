from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)   


class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE = [
        ('USER', "User"),
        ('ADMIN', "Admin"),
        ('MANAGER', "Manager"),
    ]

    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30, null=False)
    last_name = models.CharField(_('surname'), max_length=30, null=True)
    password = models.CharField(max_length=55, null=False)
    user_role = models.CharField(max_length=10, choices=USER_ROLE, default='USER') 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    
    objects = UserManager() 
       
        
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
        
        
     