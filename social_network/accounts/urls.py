from django.urls import path
from .views import register_user, user_login, UserSearchAPIView

urlpatterns = [
    path('signup/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('search/', UserSearchAPIView.as_view(), name='user-search'),
]