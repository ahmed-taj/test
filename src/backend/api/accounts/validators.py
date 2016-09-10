from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ValidationError

User = get_user_model()

# Allowed characters in username field
ALLOWED_USERNAME_CHARS = set([
    # ASCII lowercase
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z',
    # ASCII uppercase
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z',
    # Numbers & special characters
    '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '-'
])


def username_validator(username):
    m = set(username) - ALLOWED_USERNAME_CHARS
    # At lest there is one invalid char
    if m:
        raise ValidationError(_(
            'Username should contains 30 characters or fewer, '
            'including letters, digits and - only.'
        ))
    # Minimum length
    elif len(username) < 6:
        raise ValidationError(_(
            'Username should contain at least 6 characters'
        ))
    # Exists ?
    elif User.objects.filter(username=username).exists():
        raise ValidationError(_(
            'This username is already taken'
        ))


def email_validator(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError(_(
            "A user with that email address already exists."
        ))


def passwords_match(data):
    if 'password' in data:
        if data['password'] != data['confirm_password']:
            raise ValidationError({
                'confirm_password': ["Passwords don't match"]
            })
