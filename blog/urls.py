from django.urls import path

from .views import (posts, post,post_search,post_create,post_update, post_delete)

urlpatterns = [
    path('',posts),
    path('/create',post_create),
    path('/<int:post_id>/',post),
    path('/<int:post_id>/edit/',post_update),
    path('/<int:post_id>/delete/',post_delete),
    path('/<str:name>/search/',post_search),
]
