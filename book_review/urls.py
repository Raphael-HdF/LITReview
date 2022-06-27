from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name="feed"),
    path('my_posts', views.my_posts, name="my_posts"),

    path('create_ticket', views.create_ticket, name="create_ticket"),
    path('create_ticket/<int:ticket_id>', views.create_ticket, name="create_ticket"),
    path('view_ticket/<int:ticket_id>', views.view_ticket, name="view_ticket"),
    path('delete_ticket/<int:ticket_id>', views.delete_ticket, name="delete_ticket"),

    path('post_review/<int:ticket_id>', views.post_review, name="post_review"),

    path('create_review', views.create_review, name="create_review"),
    path('create_review/<int:review_id>', views.create_review, name="create_review"),
    path('view_review/<int:review_id>', views.view_review, name="view_review"),
    path('delete_review/<int:review_id>', views.delete_review, name="delete_review"),

    path('list_subscriptions', views.list_subscriptions, name="list_subscriptions"),
    path('stop_follow/<int:follow_id>', views.stop_follow, name="stop_follow"),
    path('add_follow/<int:follow_id>', views.add_follow, name="add_follow"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
