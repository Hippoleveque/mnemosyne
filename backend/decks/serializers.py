#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from decks.models import Deck

class DeckSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source="owner.email")

    def create(self,validated_data):
        return Deck.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        return instance
    