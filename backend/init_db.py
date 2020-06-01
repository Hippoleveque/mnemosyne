#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"
import django
django.setup()
import pandas as pd
from cards.models import Card
from decks.models import Deck
from users.models import User


us_history = pd.read_excel("content/us_history.xlsx","Basic")
christianity = pd.read_excel("content/christianity.xlsx","Basic")

hippo = User.objects.create_superuser(email="hippolyte.leveque@gmail.com",password="Eragon123")
franck = User.objects.create_superuser(email="franck@gmail.com",password="Eragon123")

deck_us_history = Deck(name="US History",owner=hippo)
deck_christianity = Deck(name="Christianity",owner=franck)
deck_us_history.save()
deck_christianity.save()

for row in christianity.iterrows():
    card = Card(name="",
        content_recto=row[1]["note_id"],
        content_verso=row[1]["deck_name"],
        deck=deck_christianity)
    card.save()

n = 0
for row in us_history.iterrows():
    if n > 99:
        break
    card = Card(name="",
        content_recto=row[1]["note_id"],
        content_verso=row[1]["deck_name"],
        deck=deck_us_history)
    card.save()
    n += 1