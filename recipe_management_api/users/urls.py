from django.urls import path
from .views import RegisterView, LoginView, TokenRefresh

urlpatterns = [
    path("register/", RegisterView.as_view(), name="api_register"),
    path("login/", LoginView.as_view(), name="api_login"),
    path("token/refresh/", TokenRefresh.as_view(), name="token_refresh"),
]
