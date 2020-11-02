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
      "room/<slug:room_slug>/join",
      JoinRoomAPIView.as_view(),
      name="join-room"
      ),

    path(
        'room/<slug:slug>',
        RoomDetailAPIView.as_view(),
        name='room-detail'
        ),

    path(
         "host/<int:host_id>/room/<slug:room_slug>/",
         RoomDeleteAPIView.as_view(),
         name="circle-delete"
         ),
]
