from rest_framework.throttling import UserRateThrottle
from django.core.cache import cache
from django.utils import timezone


class FriendRequestThrottle(UserRateThrottle):
    rate = '3/minute'  # Limit to 3 requests per minute

    def allow_request(self, request, view):
        if request.user.is_authenticated:
            user_id = request.user.id
            timestamp = timezone.now().timestamp()
            cache_key = f"friend_request_throttle:{user_id}"
            request_count = cache.get(cache_key, 0)
            if request_count >= 3:
                return False
            cache.set(cache_key, request_count + 1, 60)  # Cache for 60 seconds
        return True
