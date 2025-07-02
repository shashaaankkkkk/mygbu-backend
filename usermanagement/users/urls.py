# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('protected/', ProtectedView.as_view()),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
