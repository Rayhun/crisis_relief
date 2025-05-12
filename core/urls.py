# core/urls.py
from django.urls import path
from .views import views, dashboard, auth

urlpatterns = [
    path('', dashboard.DashboardView.as_view(), name='dashboard'),
    path('accounts/login/', auth.CustomLoginView.as_view(), name='login'),
    path('requests/', views.request_list_view, name='request-list'),
    path('requests/new/', views.request_create_view, name='request-create'),
    path('offers/', views.offer_list_view, name='offer-list'),
    path('offers/new/', views.offer_create_view, name='offer-create'),
]
