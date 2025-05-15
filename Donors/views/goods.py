from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Donors.forms import GoodsDonationForm


@login_required
def goods_donation_view(request):
    if request.method == "POST":
        form = GoodsDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.donation_type = 'goods'
            donation.save()
            return redirect('donation-success')
    else:
        form = GoodsDonationForm()

    return render(request, 'donate/goods_donation.html', {'form': form})
