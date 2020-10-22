from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apps.game_room.api.serializers import (CustomUserSerializer,
                                            RoomSerializer,
                                            RoomDetailSerializer
                                            )
from apps.core.utils import generate_unique_slug
from apps.game_room.models import Room, CustomUser


class CustomUserCreateAPIView(APIView):

    serializer_class = CustomUserSerializer

    def post(self, request):
        """This endpoint adds custom users to database"""

        serializer_context = {"request": request}
        serializer = self.serializer_class(
                                            data=request.data,
                                            context=serializer_context
                                          )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success': True,
                    'data': serializer.data,
                }
            )


class RoomCreateAPIView(APIView):

    serializer_class = RoomSerializer

    def post(self, request):
        """This endpoint allows a user to create a game room"""

        serializer_context = {"request": request}
        serializer = self.serializer_class(
                                            data=request.data,
                                            context=serializer_context
                                          )

        if serializer.is_valid():
            room_slug = generate_unique_slug(request.data['room_name'])
            host = get_object_or_404(CustomUser, id=request.data['host_id'])

            serializer.save(slug=room_slug, host=host)

            return Response(
                {
                    'success': True,
                    'data': serializer.data,
                }
            )


class JoinRoomAPIView(APIView):
    serializer_class = RoomSerializer

    def post(self, request, room_slug):
        """
            Allows users to  join a room.
            To join a room, this endpoint accepts a post request.
        """

        room = get_object_or_404(Room, slug=room_slug)
        user = request.user

        room.players.add(user)
        room.save()

        serializer = self.serializer_class(room)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomDetailAPIView(generics.RetrieveAPIView):
    """Gets the details of a room"""

    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = 'slug'


class RoomDeleteAPIView(APIView):

    def delete(self, request, room_slug):

        """this endpoint allows room hosts to end game session"""

        room = get_object_or_404(Room, slug=room_slug)
        request_user = request.user

        if request_user == room.super_moderator:

            room.delete()

            return Response(
                    {
                        'success': True
                    }
                )

        return Response(
                    {
                        'success': False
                    }
                )
