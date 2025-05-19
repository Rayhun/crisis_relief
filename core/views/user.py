from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import User
from core.forms import ProfileForms


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        # Only return users who are not superusers
        return User.objects.exclude(is_superuser=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get query parameter for search
        search_query = self.request.GET.get('q', '')
        if search_query and search_query == "org":
            # Filter users based on organization
            context['users'] = self.get_queryset().filter(user_type=search_query)
        elif search_query and search_query == "volunteers":
            # Filter users based on volunteer status
            context['users'] = self.get_queryset().filter(user_type=search_query)
        else:
            # Default to all users
            context['users'] = self.get_queryset()
        context['user_count'] = self.get_queryset().count()
        context['search_query'] = search_query
        return context


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'core/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # Show the profile of the currently logged-in user
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user
        form = ProfileForms(instance=user_profile)
        context['form'] = form
        return context


def update_profile(request):
    if request.method == 'POST':
        user = request.user
        form = ProfileForms(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('core:user_profile', pk=user.pk)
    return redirect('core:user_profile', pk=user.pk)
