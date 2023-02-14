from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from foodies.views import PostViewSet, UserViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'Post', PostViewSet)
router.register(r'User', UserViewSet)
router.register(r'Comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
