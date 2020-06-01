from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cards.models import Card
from decks.models import Deck
from cards.serializers import CardSerializer
from django.http import Http404
from rest_framework.views import APIView
from cards.helpers import compute_easiness_factor, compute_remaining_days
from rest_framework.permissions import IsAuthenticated
import datetime

    
class CardList(APIView):

    def get(self,request,format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        deck = Deck.objects.get(pk=request.data["deck"])
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(deck=deck)
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    

class CardDetail(APIView):

    def get_object(self,pk):
        try:
            card = Card.objects.get(pk=pk)
            return card
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk,format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card,
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CardToReview(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            card = Card.objects.get(pk=pk)
            return card
        except Card.DoesNotExist:
            return None

    def get(self,request,format=None):
        user = request.user
        cards_to_review = Card.objects.filter(deck__owner=user,
            remaining_days=0).order_by("easiness_factor")
        serializer = CardSerializer(cards_to_review,many=True)
        return Response(serializer.data)


    def patch(self,request,format=None):
        pk = request.data["uuid"]
        grade = request.data["grade"]
        card = self.get_object(pk)
        if card is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        new_ef = compute_easiness_factor(card,grade)
        new_remaining_days = compute_remaining_days(card)
        data = {"easiness_factor":new_ef,
            "remaining_days":new_remaining_days,
            "n_repeat":card.n_repeat+1,
            "last_repeat":datetime.datetime.now()}
        serializer = CardSerializer(card,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


        

