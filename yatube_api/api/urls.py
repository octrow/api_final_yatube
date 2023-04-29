from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

routerv1 = DefaultRouter()

routerv1.register(r"posts", PostViewSet, basename="posts")
routerv1.register(r"groups", GroupViewSet, basename="groups")
routerv1.register(r"follow", FollowViewSet, basename="follow")
routerv1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)


urlpatterns = [
    path("v1/", include(routerv1.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
