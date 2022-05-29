from django.urls import path

from book_review import views

urlpatterns = [
    path('', views.list_reviews, nom="list_reviews"),
]
