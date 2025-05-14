from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View # noqa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, TaskComment
from core.models import User


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10  # Number of tasks per page
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get pk from keyword arguments
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        task = self.model.objects.filter(user=user)
        context['tasks'] = task
        context['user'] = user
        context['task_count'] = task.count()
        return context
