from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, TaskComment
from Affected.models import ReliefRequest
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
        context['open_tasks'] = task.filter(status='open')
        context['user'] = user
        context['task_count'] = task.count()
        return context


def task_self_assign(request, pk):
    try:
        relief_request = ReliefRequest.objects.get(pk=pk, status='open')
    except Exception as e:
        print(e)
        return redirect('task:task_list', pk=request.user.pk)
    Task.objects.create(
        user=request.user,
        title=relief_request.title,
        description=f"Location: {relief_request.location}\n \n {relief_request.description}", # noqa
        status='open',
    )
    relief_request.status = 'in_progress'
    relief_request.save()
    return redirect('task:task_list', pk=request.user.pk)