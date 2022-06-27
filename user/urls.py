from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register_user/', views.register_user, name="register_user"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
