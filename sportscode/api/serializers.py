from rest_framework import serializers
from .models import User, BettingCode, Message, Location

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'emial']

#BetCode Serializer
class BettingCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingCode
        fields = ['id', 'user', 'original_code', 'converted_code', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},
        }

#Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'message', 'sent_at']
        extra_kwargs = {
            'user': {'read_only': True},
        }

#Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'user', 'latitude', 'longitude', 'timestamp']
        extra_kwargs = {
            'user': {'read_only': True},
        }