#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("",views.UserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)