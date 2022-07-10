from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _

from book_review.forms import PostReviewForm, TicketForm
from book_review.models import Ticket, Review


@login_required()
def post_review(request, ticket_id=None, review_id=None):
    ticket = get_object_or_404(Ticket, pk=ticket_id) if ticket_id else None

    review = get_object_or_404(Review, pk=review_id, user=request.user) if \
        review_id else None
    title = _("Modify your review") if review else _("Create your review")

    ticket_form = TicketForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
        instance=ticket)
    review_form = PostReviewForm(
        request.POST if request.method == "POST" else None,
        instance=review
    )

    if request.method == 'GET':
        return render(request, 'review/post_review.html', locals())
    elif request.method == 'POST':
        if review_form.is_valid():
            if ticket_form and ticket_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
        else:
            return render(request, 'review/post_review.html', locals())
    return redirect('feed')


@login_required()
def view_review(request, review_id):
    reviews = [get_object_or_404(Review, pk=review_id)]
    return render(request, 'review/view_review.html', {'reviews': reviews})


@login_required()
def delete_review(request):
    if request.method == "POST" and request.POST.get("delete_review_id"):
        review = get_object_or_404(Review, pk=request.POST.get("delete_review_id"))
        review.delete()
    else:
        messages.warning(request, _("Your review has'nt been deleted"))
    return redirect('my_posts')
