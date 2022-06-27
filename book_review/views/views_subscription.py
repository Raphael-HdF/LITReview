from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from book_review.models import UserFollows
from user.models import User


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
        if request.POST.get("unscribe"):
            stop_follow(request, request.POST.get("unscribe"))
        elif request.POST.get("subscribe"):
            add_follow(request, request.POST.get("subscribe"))
        else:
            follower = request.POST.get('follower')
            actual_followers = [follower.followed_user.id for follower in
                                UserFollows.objects.filter(user=request.user)]
            find_followers = User.objects.filter(username__icontains=follower) \
                .exclude(pk=request.user.id).exclude(pk__in=actual_followers)
            vals |= {'find_followers': find_followers}
    vals |= {
        'followed_users': UserFollows.objects.filter(user=request.user),
        'followers': UserFollows.objects.filter(followed_user=request.user),
    }
    return render(request, 'subscription/list_subscriptions.html', vals)
