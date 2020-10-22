from rest_framework import serializers

from apps.game_room.models import CustomUser, Room


class CustomUserSerializer(serializers.ModelSerializer):
    """ This serialiazes a custom user"""

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    points = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'points']


class RoomSerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True)
    room_name = serializers.CharField(required=False)

    class Meta:
        model = Room
        fields = [
                  'slug', 'room_name'
                  ]


class RoomDetailSerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True)
    room_name = serializers.CharField(required=False)

    players_count = serializers.SerializerMethodField()

    host = serializers.StringRelatedField(read_only=True)

    invite_link = serializers.CharField(
                                        max_length=500,
                                        read_only=True
                                        )
    players = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
                  'slug', 'room_name',
                  'players_count', 'host',
                  'invite_link', 'players'
                  ]

    def get_players_count(self, object):
        return object.players.count()

    def get_players(self, object):
        return object.players.all()
