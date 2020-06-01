from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decks.models import Deck
from decks.serializers import DeckSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class DeckList(APIView):

    def get(self,request,format=None):
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    

class DeckDetail(APIView):

    def get_object(self,pk):
        try:
            deck = Deck.objects.get(pk=pk)
        except Deck.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return deck
    
    def get(self,request,pk,format=None):
        deck = self.get_object(pk)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        deck = self.get_object(pk)
        serializer = DeckSerializer(deck,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        deck = self.get_object(pk)
        deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DecksToReview(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            deck = Deck.object.get(pk=pk)
            return deck
        except Deck.DoesNotExist:
            return None
        
    


    def get(self,request,format=None):
        user = request.user
        decks_to_review = Deck.objects.filter(owner=user)
        serializer = DeckSerializer(decks_to_review,many=True)
        return Response(serializer.data)
    


