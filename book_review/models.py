from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    description = models.TextField(_('Description'), max_length=2048, blank=True)
    user = models.ForeignKey(verbose_name=_('User'), to=get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), null=True, blank=True, upload_to="tickets")
    time_created = models.DateTimeField(_('Created time'), auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_ticket', kwargs={"ticket_id": self.id})

    def answered(self):
        if self.review_set.count():
            return True
        return False

    def get_last_review_id(self):
        return self.review_set.last().id

class Review(models.Model):

    ticket = models.ForeignKey(verbose_name=_('Ticket'), to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        _('Rating'),
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        default=0
    )
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=get_user_model(), on_delete=models.CASCADE)
    headline = models.CharField(_('Headline'), max_length=128)
    body = models.CharField(_('Body'), max_length=8192, blank=True)
    time_created = models.DateTimeField(_('Created time'), auto_now_add=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('view_review', kwargs={"review_id": self.id})

    def inverse_rating(self):
        return 5 - self.rating


class UserFollows(models.Model):
    user = models.ForeignKey(verbose_name=_('Follower'), to=get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(verbose_name=_('Followed user'), to=get_user_model(),
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')

    def __str__(self):
        return self.user.username + ' - ' + self.followed_user.username

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
