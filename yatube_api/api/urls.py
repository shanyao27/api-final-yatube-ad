from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, GroupViewSet,
                    FollowViewSet, PostViewSet)


app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
