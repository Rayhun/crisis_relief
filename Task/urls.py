from django.urls import path
from .views import TaskListView, task_self_assign, task_update, update_checklist, update_task_status, TaskDetailView

app_name = 'task'


urlpatterns = [
    path('task/self-assign/<int:pk>/', task_self_assign, name='task_self_assign'),
    path('task/update/<int:pk>/', task_update, name='task_update'),
    path('<int:task_id>/update_checklist/', update_checklist, name='update_checklist'),
    path('tasks/<int:task_id>/<str:new_status>/update_status/', update_task_status, name='update_task_status'),
    path('tasks/<int:pk>/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/details/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
]
