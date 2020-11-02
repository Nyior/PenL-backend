import random
import string


ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    """function that generates a random string"""

    return "".join(random.choice(chars) for _ in range(length))


def generate_unique_slug(word):

    alphanumeric = ''

    for character in word:
        if character == " ":
            alphanumeric += "-"

        if character == "-":
            pass

        if character.isalnum():
            alphanumeric += character

    return alphanumeric + generate_random_string()


def generate_unique_invite_link(slug):

    invite_link = f'http://localhost:8080/join-room?room_slug={slug}'
    return invite_link

# https://pnl-ng.netlify.app/
