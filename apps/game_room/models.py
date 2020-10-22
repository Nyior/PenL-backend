from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from apps.core.utils import generate_unique_invite_link


class Room(models.Model):
    """ This class models a game room object
    """
    slug = models.SlugField(max_length=255, primary_key=True)
    room_name = models.CharField(max_length=50)
    host = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                related_name="room_host_in",
                                null=True
                                )
    invite_link = models.CharField(max_length=500, null=True)

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        self.players.add(self.host)
        self.invite_link = generate_unique_invite_link(self.slug)

    def __str__(self):
        return self.room_name


class CustomUser(AbstractUser):
    """ This class models a pnl user
    """
    points = models.IntegerField(null=True, default=0)
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name="players",
                             null=True
                             )
