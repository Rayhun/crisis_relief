from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from Affected.models import ReliefRequest
from Affected.forms import RequestForm


class ReliefRequestListView(LoginRequiredMixin, ListView):
    """
    View to list all relief requests.
    """
    model = ReliefRequest
    template_name = 'affected/relief_request_list.html'
    context_object_name = 'relief_requests'
    paginate_by = 10

    def get_queryset(self):
        return ReliefRequest.objects.all()


class ReliefRequestDetailView(LoginRequiredMixin, DetailView):
    """
    View to display details of a specific relief request.
    """
    model = ReliefRequest
    template_name = 'affected/relief_request_detail.html'
    context_object_name = 'relief_request'


class ReliefRequestCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new relief request.
    """
    model = ReliefRequest
    form_class = RequestForm
    template_name = 'affected/relief_request_form.html'
    success_url = reverse_lazy('affected:relief_request_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReliefRequestUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update an existing relief request.
    """
    model = ReliefRequest
    form_class = RequestForm
    template_name = 'affected/relief_request_form.html'
    success_url = reverse_lazy('affected:relief_request_list')

    def get_queryset(self):
        return ReliefRequest.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReliefRequestDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a relief request.
    """
    model = ReliefRequest
    template_name = 'affected/relief_request_confirm_delete.html'
    success_url = reverse_lazy('affected:relief_request_list')

    def get_queryset(self):
        return ReliefRequest.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relief_request'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('affected:relief_request_list')
