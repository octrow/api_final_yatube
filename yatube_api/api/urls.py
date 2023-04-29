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
    path("", include(routerv1.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
