import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Donation
from core.models import User
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def donation_page(request):
    return render(request, 'donate/donation.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })


@login_required
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))

        if amount < 5:
            return JsonResponse(
                {'error': 'Minimum donation amount is $5'}, status=400
            )

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Donation',
                        },
                        'unit_amount': amount * 100,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/donate/donation-success/'), # noqa
                cancel_url=request.build_absolute_uri('/donate/donation-cancelled/'), # noqa
                metadata={'user_id': request.user.id},
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def success_view(request):
    return render(request, 'donate/donation_success.html')


def cancel_view(request):
    return render(request, 'donate/donation_cancelled.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        amount = int(session['amount_total']) / 100
        payment_intent = session['payment_intent']
        user_id = session['metadata'].get('user_id')

        try:
            user = User.objects.get(id=user_id)

            Donation.objects.get_or_create(
                stripe_payment_intent=payment_intent,
                defaults={
                    'amount': amount,
                    'donor': user,
                }
            )
        except User.DoesNotExist:
            pass  # optionally log this

    return HttpResponse(status=200)
