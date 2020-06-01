from django.db import models
from uuid import uuid4
from decks.models import Deck


class Card(models.Model):
    """ Base Card """
    uuid = models.UUIDField(primary_key=True, default=uuid4, 
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    content_recto = models.CharField(max_length=1000)
    content_verso = models.CharField(max_length=1000)
    easiness_factor = models.FloatField(default=2.5)
    last_repeat = models.DateTimeField(auto_now=True)
    remaining_days = models.IntegerField(default=0)
    n_repeat = models.IntegerField(default=0)
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE,
        related_name="cards")
    class Meta:
        ordering = ["deck","easiness_factor"]


