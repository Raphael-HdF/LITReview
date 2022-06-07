from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    # path('create_ticket/<int:ticket_id>', views.create_ticket, name="create_ticket"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)