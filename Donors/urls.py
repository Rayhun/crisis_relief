from django.urls import path
from . import views

app_name = 'donate'


urlpatterns = [
    path('donate/', views.donation_page, name='donation_page'),
    path('create-checkout-session/', views.create_checkout_session,
         name='create_checkout_session'),
    path('donation-success/', views.success_view, name='donation_success'),
    path('donation-cancelled/', views.cancel_view, name='donation_cancelled'),

    # webhook
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
]
