from django.db import models

from chat_bot_project.chatbot_cards.models import Bots

class Bot_favourites(models.Model):
    bot_favourites = models.ManyToManyField(Bots, blank=True)

