from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import django.contrib.auth.models as auth


class Account(auth.AbstractBaseUser, auth.PermissionsMixin):
    """
    Custom account model that behaves like Django default one.
    """
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_(
            'Username should contains 30 characters or fewer, '
            'including letters, digits and - only.'
        )
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this '
            'admin site.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = auth.UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the account."
        return self.first_name
