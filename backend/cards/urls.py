#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from cards import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("",views.CardList.as_view()),
    path("<uuid:pk>/",views.CardDetail.as_view()),
    path("reviews/",views.CardToReview.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)