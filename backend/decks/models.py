from django.db import models
from uuid import uuid4
from users.models import User


class Deck(models.Model):
    """ Base Deck """
    uuid = models.UUIDField(primary_key=True, default=uuid4, 
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,
        related_name="decks")

    class Meta:
        ordering = ["created_at"]


