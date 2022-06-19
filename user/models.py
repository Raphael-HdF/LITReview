from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    description = models.TextField(_('User description'), max_length=2048, blank=True)
    # is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
