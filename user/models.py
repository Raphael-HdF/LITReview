import objects as objects
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, username, password, **other_fields):
#         if not email:
#             raise ValueError(_('Please enter your email address'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, password=password, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, username, password, **other_fields):
#         other_fields['is_superuser'] = True
#         other_fields['is_staff'] = True
#         other_fields['is_active'] = True
#
#         return self.create_user(email, username, password, **other_fields)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    description = models.TextField(_('User description'), max_length=2048, blank=True)
    # is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
