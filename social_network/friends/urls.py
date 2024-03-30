from django.urls import path
from .views import SendFriendRequestAPIView, AcceptFriendRequestAPIView, RejectFriendRequestAPIView, ListFriendsAPIView, ListPendingFriendRequestsAPIView

urlpatterns = [
    path('send-request/', SendFriendRequestAPIView.as_view(), name='send-friend-request'),
    path('accept-request/<int:pk>/', AcceptFriendRequestAPIView.as_view(), name='accept-friend-request'),
    path('reject-request/<int:pk>/', RejectFriendRequestAPIView.as_view(), name='reject-friend-request'),
    path('list-friends/', ListFriendsAPIView.as_view(), name='list-friends'),
    path('list-pending-friend-requests/', ListPendingFriendRequestsAPIView.as_view(), name='list-pending-friend-requests'),
]
