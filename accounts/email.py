from djoser.email import ConfirmationEmail as BaseConfirmationEmail
from django.shortcuts import render
from django.core import mail
from django.views.generic.base import ContextMixin


class ConfirmationEmail(BaseConfirmationEmail):
    template_name = 'confirmation.html'
    
    