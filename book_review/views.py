from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm
from .models import Ticket, UserFollows
from user.models import User


@login_required()
def list_reviews(request):
    vals = {'tickets': Ticket.objects.all()}
    return render(request, 'list_reviews.html', vals)


@login_required()
def create_ticket(request, ticket_id=None):
    instance_ticket = Ticket.objects.get(pk=ticket_id) if ticket_id is not None else None
    if request.method == 'GET':
        form = TicketForm(instance=instance_ticket)
        return render(request, 'create_ticket.html', locals())
    elif request.method == 'POST':
        form = TicketForm(request.POST, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
    return redirect('list_reviews')


@login_required()
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'view_ticket.html', locals())


@login_required()
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    return redirect('list_reviews')


@login_required()
def add_follow(request, follow_id):
    follow = get_object_or_404(User, pk=follow_id)
    following = UserFollows(user=request.user, followed_user=follow)
    following.save()
    return redirect('list_subscriptions')


@login_required()
def stop_follow(request, follow_id):
    follow = get_object_or_404(UserFollows, pk=follow_id)
    follow.delete()
    return redirect('list_subscriptions')


@login_required()
def list_subscriptions(request):
    vals = {}
    if request.method == "POST":
        follower = request.POST.get('follower')
        actual_followers = [follower.followed_user.id for follower in UserFollows.objects.filter(user=request.user)]
        find_followers = User.objects.filter(username__icontains=follower)\
            .exclude(pk=request.user.id).exclude(pk__in=actual_followers)
        vals |= {'find_followers': find_followers}
    vals |= {
        'followed_users': UserFollows.objects.filter(user=request.user),
        'followers': UserFollows.objects.filter(followed_user=request.user),
    }
    return render(request, 'list_subscriptions.html', vals)
