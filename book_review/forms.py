from django.forms import ModelForm
from django import forms
from book_review.models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        widgets = {'image': forms.FileInput}
        model = Ticket
        fields = ['title', 'description', 'image', ]


class ReviewForm(ModelForm):
    class Meta:
        widgets = {
            'rating': forms.RadioSelect(attrs={
                'class': 'd-flex justify-content-around'
            }),
            'body': forms.Textarea(),
        }
        model = Review
        fields = ['ticket', 'headline', 'rating', 'body', ]


class PostReviewForm(ModelForm):
    class Meta:
        widgets = {
            'rating': forms.RadioSelect(attrs={
                'class': 'd-flex justify-content-around'
            }),
            'body': forms.Textarea(),
        }
        model = Review
        fields = ['headline', 'rating', 'body', ]
