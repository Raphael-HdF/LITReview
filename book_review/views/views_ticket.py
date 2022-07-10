from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from book_review.forms import TicketForm
from book_review.models import Ticket


@login_required()
def create_ticket(request, ticket_id=None):
    instance_ticket = Ticket.objects.get(
        pk=ticket_id) if ticket_id else None
    main_h1 = _("Modify your ticket") if instance_ticket else _("Create your ticket")
    if request.method == 'GET':
        form = TicketForm(instance=instance_ticket)
        image = instance_ticket.image if instance_ticket else None
        return render(request, 'ticket/create_ticket.html', locals())
    elif request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
    return redirect('my_posts')


@login_required()
def view_ticket(request, ticket_id):
    tickets = [get_object_or_404(Ticket, pk=ticket_id)]
    return render(request, 'ticket/view_ticket.html', {'tickets': tickets})


@login_required()
def delete_ticket(request):
    if request.method == "POST" and request.POST.get("delete_ticket_id"):
        ticket = get_object_or_404(Ticket, pk=request.POST.get("delete_ticket_id"))
        ticket.delete()
    else:
        messages.warning(request, _("Your ticket has'nt been deleted"))
    return redirect('my_posts')
