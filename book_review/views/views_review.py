from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _

from book_review.forms import PostReviewForm, TicketForm
from book_review.models import Ticket, Review


@login_required()
def create_review(request, review_id=None):
    instance_review = Review.objects.get(
        pk=review_id) if review_id is not None else None
    instance_ticket = instance_review.ticket if instance_review else None
    title = _("Modify your review") if instance_review else _("Create your review")
    if request.method == 'GET':
        ticket_form = TicketForm(instance=instance_ticket)
        review_form = PostReviewForm(instance=instance_review)
        return render(request, 'review/create_review.html', {
            'ticket_form': ticket_form,
            'review_form': review_form,
            'main_h1': title
        })
    elif request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        review_form = PostReviewForm(request.POST, instance=instance_review)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
    return redirect('my_posts')


@login_required()
def post_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    instance_review = Review.objects.get(
        ticket_id=ticket_id, user_id=request.user.id
    )
    title = _("Modify your review") if instance_review else _("Create your review")

    if request.method == 'GET':
        form = PostReviewForm(instance=instance_review)
        return render(request, 'review/post_review.html',
                      {
                          'form': form,
                          'ticket': ticket,
                          'main_h1': title,
                      })
    elif request.method == 'POST':
        form = PostReviewForm(request.POST, instance=instance_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
        else:
            return render(request, 'review/post_review.html',
                          {
                              'form': form,
                              'ticket': ticket,
                              'main_h1': title,
                          })
    return redirect('feed')


@login_required()
def view_review(request, review_id):
    reviews = [get_object_or_404(Review, pk=review_id)]
    return render(request, 'review/view_review.html', {'reviews': reviews})


@login_required()
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('my_posts')
