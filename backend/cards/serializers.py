#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from cards.models import Card


class CardSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=200)
    content_recto = serializers.CharField(max_length=1000)
    content_verso = serializers.CharField(max_length=1000)
    last_repeat = serializers.DateTimeField()
    remaining_days = serializers.IntegerField()
    n_repeat = serializers.IntegerField()
    easiness_factor = serializers.FloatField(required=False)
    deck_name = serializers.ReadOnlyField(source="deck.name")
    owner = serializers.ReadOnlyField(source="deck.owner.email")

    def create(self,validated_data):
        return Card.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.content = validated_data.get("content",instance.content)
        instance.easiness_factor = validated_data.get("easiness_factor",instance.easiness_factor)
        instance.last_repeat = validated_data.get("last_repeat",instance.last_repeat)
        instance.remaining_days = validated_data.get("remaining_days",instance.remaining_days)
        instance.n_repeat = validated_data.get("n_repeat",instance.n_repeat)
        instance.save()
        return instance
    