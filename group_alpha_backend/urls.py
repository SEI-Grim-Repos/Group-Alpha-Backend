from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from foodies.views import PostViewSet, CommentViewSet, User_AccountViewSet

router = routers.DefaultRouter()
# router.register(r'User-Account', User_AccountViewSet, basename='user')
# router.register(r'Post', PostViewSet)

router.register(r'profiles', User_AccountViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('foodies.urls')),
    path('user/', include('user_auth.urls')),
    path('admin/', admin.site.urls),
]
