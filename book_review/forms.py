from django.forms import ModelForm
from book_review.models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'headline', 'rating', 'body', ]
