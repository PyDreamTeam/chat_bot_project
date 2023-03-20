from django.db import models
from accounts.models import User
from chatbot_cards.models import Bots

from chat_bot_project.chatbot_cards.models import Bots

class Bot_favourites(models.Model):
    bot_favourites = models.ManyToManyField(Bots, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def display_products(self):
        return ', '.join([bots.title for bots in self.bot_favourites.all()])

