#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


def compute_remaining_days(card):
    if card.n_repeat == 0:
        return 0
    elif card.n_repeat == 1:
        return 1
    elif card.n_repeat == 2:
        return 6
    else:
        now = datetime.datetime.now(datetime.timezone.utc)
        last_interval = (now - card.last_repeat).days
        return last_interval * card.easiness_factor


def compute_easiness_factor(card, grade):
    new_ef = card.easiness_factor + (0.1-(5-grade)*(0.08+(5-grade)*0.02))
    if new_ef < 1.3:
        new_ef = 1.3
    elif new_ef > 2.5:
        new_ef = 2.5
    return new_ef
