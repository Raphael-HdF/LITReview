from django.urls import path

from book_review import views

urlpatterns = [
    path('', views.list_reviews, name="list_reviews"),
    path('create_ticket', views.create_ticket, name="create_ticket"),
    path('create_ticket/<int:ticket_id>', views.create_ticket, name="create_ticket"),
    path('view_ticket/<int:ticket_id>', views.view_ticket, name="view_ticket"),
    path('delete_ticket/<int:ticket_id>', views.delete_ticket, name="delete_ticket"),
]
