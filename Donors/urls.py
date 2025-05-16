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
    path(
        'goods-donation-list/', goods.GoodsDonationListView.as_view(),
        name='goods_donation_list'
    ),
    path(
        'goods-donation-create/', goods.GoodsDonationCreateView.as_view(),
        name='goods_donation_create'
    ),
    path(
        'goods-donation-details/<int:pk>/',
        goods.DonationDeleteView.as_view(), name="goods_donation_details"
    )
]
