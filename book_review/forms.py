from django.forms import ModelForm
from book_review.models import Ticket


class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]


