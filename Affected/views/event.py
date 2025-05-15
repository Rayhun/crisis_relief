from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from Affected.models import Event, ReliefRequest
from Affected.forms import EventForm


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'
    login_url = '/login/'

    def get_queryset(self):
        return Event.objects.all()


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relief_requests'] = ReliefRequest.objects.filter(
            event=self.object
        )
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/event_form.html'
    success_url = reverse_lazy('affected:event_list')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MapEventCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST.get('date'), "#" * 20)
        event = Event.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            event_type=request.POST.get('event_type'),
            specific_details=request.POST.get('specific_details'),
            intensity=request.POST.get('intensity'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
            location=request.POST.get('location'),
            radius=request.POST.get('radius'),
            affected_people=request.POST.get('affected_people'),
        )
        return redirect(reverse_lazy('core:albania_map'))


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event/event_form.html'
    success_url = reverse_lazy('affected:event_list')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event/event_confirm_delete.html'
    success_url = reverse_lazy('affected:event_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relief_requests'] = ReliefRequest.objects.filter(
            event=self.object
        )
        return context
