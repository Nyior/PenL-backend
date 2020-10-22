from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.game_room.models import CustomUser, Room


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'points']


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ['room_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room, RoomAdmin)
