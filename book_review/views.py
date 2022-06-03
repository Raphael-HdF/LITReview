from django.shortcuts import render, redirect, get_object_or_404

from book_review.forms import TicketForm
from book_review.models import Ticket


def list_reviews(request):
    vals = {'tickets': Ticket.objects.all()}
    return render(request, 'list_reviews.html', vals)


def create_ticket(request, ticket_id=None):
    instance_ticket = Ticket.objects.get(pk=ticket_id) if ticket_id is not None else None
    if request.method == 'GET':
        form = TicketForm(instance=instance_ticket)
        return render(request, 'create_ticket.html', locals())
    elif request.method == 'POST':
        form = TicketForm(request.POST, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect('list_reviews')


def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'view_ticket.html', locals())

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete(ticket_id)
    return redirect('list_reviews')
