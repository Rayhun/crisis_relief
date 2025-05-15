from django.urls import path
from .views import money, goods

app_name = 'donate'


urlpatterns = [
    path('donate/', money.donation_page, name='donation_page'),
    path('create-checkout-session/', money.create_checkout_session,
         name='create_checkout_session'),
    path('donation-success/', money.success_view, name='donation_success'),
    path('donation-cancelled/', money.cancel_view, name='donation_cancelled'),

    # webhook
    path('stripe/webhook/', money.stripe_webhook, name='stripe_webhook'),

    # Goods donation
    path('goods-donation/', goods.goods_donation_view, name='goods_donation'),
]
