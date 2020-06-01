#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from decks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("",views.DeckList.as_view()),
    path("<uuid:pk>/",views.DeckDetail.as_view()),
    path("reviews/",views.DecksToReview.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)