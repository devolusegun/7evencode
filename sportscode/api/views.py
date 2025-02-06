from django.shortcuts import render
from rest_framework import generics, permissions
from .models import BettingCode, Message, Location
from .serializers import BettingCodeSerializer, MessageSerializer, LocationSerializer


# BettingCode View
class BettingCodeListCreate(generics.ListCreateAPIView):
    queryset = BettingCode.objects.all()
    serializer_class = BettingCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BettingCodeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BettingCode.objects.all()
    serializer_class = BettingCodeSerializer
    permission_classes = [permissions.IsAuthenticated]


#MessageView
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


#Location View
class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

