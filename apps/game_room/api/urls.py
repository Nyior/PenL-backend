from django.urls import path
from apps.game_room.api.views import (
                                       CustomUserCreateAPIView,
                                       RoomCreateAPIView,
                                       JoinRoomAPIView,
                                       RoomDetailAPIView,
                                       RoomDeleteAPIView
                                      )

urlpatterns = [
    path('user', CustomUserCreateAPIView.as_view(), name='new-user'),

    path('room', RoomCreateAPIView.as_view(), name='new-room'),

    path(
      "room/<slug:room_slug>/join/",
      JoinRoomAPIView.as_view(),
      name="join-room"
      ),

    path(
        'room/<slug:slug>',
        RoomDetailAPIView.as_view(),
        name='room-detail'
        ),

    path(
         "room/<slug:slug>/delete/",
         RoomDeleteAPIView.as_view(),
         name="circle-delete"
         ),
]
