from django.contrib import admin
from .models import Ticket, Review, UserFollows


@admin.register(Ticket)
class TicketAdminConfig(admin.ModelAdmin):
    model = Ticket
    search_fields = ('title', 'user',)
    list_filter = ('user',)
    ordering = ('-time_created',)
    list_display = ('title', 'user',)


@admin.register(Review)
class ReviewAdminConfig(admin.ModelAdmin):
    model = Review
    search_fields = ('ticket', 'user', 'headline')
    list_filter = ('user', 'rating',)
    ordering = ('-time_created',)
    list_display = ('headline', 'user', 'ticket', 'rating',)


@admin.register(UserFollows)
class UserFollowsAdminConfig(admin.ModelAdmin):
    model = UserFollows
    search_fields = ('user', 'followed_user',)
    list_filter = ('user', 'followed_user',)
    ordering = ('user',)
    list_display = ('user', 'followed_user',)
