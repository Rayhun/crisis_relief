# core/urls.py
from django.urls import path
from .views import dashboard, auth

app_name = 'core'

urlpatterns = [
    path('', dashboard.DashboardView.as_view(), name='dashboard'),
    path('login/', auth.CustomLoginView.as_view(), name='login'),
    path('signup/', auth.SignupView.as_view(), name='signup'),
]
