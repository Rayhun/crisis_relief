from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, TaskComment, Tag
from Affected.models import ReliefRequest
from core.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


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
        context['all_tags'] = Tag.objects.all()
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


def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.affected_people = request.POST.get('affected_people')
        task.description = request.POST.get('description')
        task.save()

        tag_ids = request.POST.getlist('tags')
        task.tags.set(Tag.objects.filter(id__in=tag_ids))
        return redirect('task:task_list', pk=request.user.pk)
 
    except Exception as e:
        print(e)
        return redirect('task:task_list', pk=request.user.pk)


@csrf_exempt
def update_checklist(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)

        description = task.description

        for item in data['checklist_items']:
            text_content = item['text'].strip()

            # Pattern for unchecked item with HTML tags
            unchecked_pattern = re.compile(
                r'<p>- \[ \]' + re.escape(text_content) + r'<\/p>|'
                r'- \[ \]' + re.escape(text_content) + r'<br>'
            )

            # Pattern for checked item with HTML tags
            checked_pattern = re.compile(
                r'<p>- \[x\]' + re.escape(text_content) + r'<\/p>|'
                r'- \[x\]' + re.escape(text_content) + r'<br>'
            )

            if item['checked']:
                # Replace all variants of unchecked items
                description = unchecked_pattern.sub(
                    f'<p>- [x]{text_content}</p>',
                    description
                )
            else:
                # Replace all variants of checked items
                description = checked_pattern.sub(
                    f'<p>- [ ]{text_content}</p>',
                    description
                )

        task.description = description
        task.save()
        return JsonResponse({
            'status': 'success',
            'new_description': description  # For debugging
        })

    return JsonResponse({'status': 'error'}, status=400)


@require_POST
@csrf_exempt
def update_task_status(request, task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        if new_status in ['open', 'in_progress', 'closed']:
            task.status = new_status
            task.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid status'})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'})
