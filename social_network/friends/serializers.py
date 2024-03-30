from rest_framework import serializers
from .models import FriendRequest
from .models import Friendship


class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver', 'status', 'created_at']


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['user1', 'user2', 'created_at']
