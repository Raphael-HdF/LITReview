from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name="feed"),
    path('list_reviews', views.list_reviews, name="list_reviews"),
    path('create_ticket', views.create_ticket, name="create_ticket"),
    path('create_ticket/<int:ticket_id>', views.create_ticket, name="create_ticket"),
    path('view_ticket/<int:ticket_id>', views.view_ticket, name="view_ticket"),
    path('delete_ticket/<int:ticket_id>', views.delete_ticket, name="delete_ticket"),
    path('list_subscriptions', views.list_subscriptions, name="list_subscriptions"),
    path('stop_follow/<int:follow_id>', views.stop_follow, name="stop_follow"),
    path('add_follow/<int:follow_id>', views.add_follow, name="add_follow"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
