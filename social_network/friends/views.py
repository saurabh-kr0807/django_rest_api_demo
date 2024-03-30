from rest_framework import generics, status
from rest_framework.response import Response
from .models import FriendRequest
from .serializers import FriendRequestSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Friendship
from .serializers import FriendshipSerializer
from .throttles import FriendRequestThrottle
from rest_framework.exceptions import PermissionDenied


class SendFriendRequestAPIView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class AcceptFriendRequestAPIView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.receiver:
            raise PermissionDenied("You are not authorized to accept this friend request.")
        instance.accept()
        Friendship.objects.create(user1=instance.sender, user2=instance.receiver)
        return Response({'status': 'Friend request accepted'}, status=status.HTTP_200_OK)


class RejectFriendRequestAPIView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.receiver:
            raise PermissionDenied("You are not authorized to reject this friend request.")
        instance.reject()
        Friendship.objects.filter(user1=instance.sender, user2=instance.receiver).delete()
        return Response({'status': 'Friend request rejected'}, status=status.HTTP_200_OK)


class ListFriendsAPIView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = Friendship.objects.filter(user1=user) | Friendship.objects.filter(user2=user)
        return friends


class ListPendingFriendRequestsAPIView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        pending_requests = FriendRequest.objects.filter(sender=user, status='pending')
        return pending_requests
