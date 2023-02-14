from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from foodies.views import UserViewSet, PostViewSet, CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Post', PostViewSet)
router.register(r'Comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
