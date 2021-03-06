from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Value, CharField
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.core.paginator import Paginator
from django.db.models import FilteredRelation, Q

from book_review.models import Ticket, UserFollows, Review
from user.models import User


def get_users_viewable_reviews(users):
    reviews = Review.objects.filter(user__in=users)
    return reviews


def get_users_linked_reviews(users, user):
    linked_reviews = Review.objects.filter(user__in=users) | Review.objects.filter(Q(
        ticket__user=user), ~Q(user=user))
    return linked_reviews


def get_users_viewable_tickets(users):
    tickets = Ticket.objects.filter(user__in=users)
    return tickets


def get_followed_user_ids(user):
    user_id = user.id if isinstance(user, User) else user
    followed_users_ids = [followed.followed_user for followed in
                          UserFollows.objects.filter(user=user_id)]
    user = User.objects.get(pk=user_id)
    followed_users_ids.append(user)
    return followed_users_ids


@login_required()
def feed(request):
    followed_users_ids = get_followed_user_ids(request.user)
    reviews = get_users_linked_reviews(followed_users_ids, request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(followed_users_ids)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    p = Paginator(posts, 5)
    page = request.GET.get('page')
    actual_posts = p.get_page(page)

    return render(request, 'feed/feed.html', context={
        'posts': actual_posts,
        'main_h1': _("Feed")
    })


@login_required()
def my_posts(request):
    reviews = Review.objects.filter(user=request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user=request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    p = Paginator(posts, 5)
    page = request.GET.get('page')
    actual_posts = p.get_page(page)

    return render(request, 'feed/feed.html',
                  context={
                      'posts': actual_posts,
                      'main_h1': _("My Posts")
                  })
