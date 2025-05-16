from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Donation
from Donors.forms import GoodsDonationForm


class GoodsDonationListView(LoginRequiredMixin, ListView):
    model = Donation
    template_name = 'donate/goods_donation_list.html'
    context_object_name = 'donations'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation = Donation.objects.filter(donation_type='goods')
        if donation.exists() and self.request.user.is_superuser:
            context['donations'] = donation
        else:
            context['donations'] = donation.filter(donor=self.request.user)
        return context


class GoodsDonationCreateView(LoginRequiredMixin, CreateView):
    model = Donation
    form_class = GoodsDonationForm
    template_name = 'donate/goods_donation_form.html'
    success_url = reverse_lazy('donate:goods_donation_list')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.donor = self.request.user
        form.instance.donation_type = 'goods'
        return super().form_valid(form)


class DonationDeleteView(LoginRequiredMixin, DetailView):
    model = Donation
    template_name = 'donate/goods_donation_details.html'
    success_url = reverse_lazy('donate:goods_donation_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['object'] = self.model.objects.get(pk=pk)
        return context
