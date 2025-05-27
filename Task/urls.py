from django.urls import path
from .views import (
    TaskListView, task_self_assign, task_update, update_checklist,
    update_task_status, TaskDetailView, TaskCommentView, volunteers_request_view,
    VolunteersRequestListView, volunteers_request_approve, volunteers_request_reject,
    VolunteersRequestDetailView
)

app_name = 'task'


urlpatterns = [
    path('task/self-assign/<int:pk>/', task_self_assign, name='task_self_assign'),
    path('task/update/<int:pk>/', task_update, name='task_update'),
    path('<int:task_id>/update_checklist/', update_checklist, name='update_checklist'),
    path('tasks/<int:task_id>/<str:new_status>/update_status/', update_task_status, name='update_task_status'),
    path('tasks/<int:pk>/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/details/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('comment/<int:pk>/', TaskCommentView.as_view(), name='task_comment'),
    path('volunteers/request/<int:pk>/', volunteers_request_view, name='volunteers_request'),
    path('volunteers/request/list/', VolunteersRequestListView.as_view(), name='volunteers_request_list'),
    path('volunteers/request/<int:pk>/approve/', volunteers_request_approve, name='volunteers_request_approve'),
    path('volunteers/request/<int:pk>/reject/', volunteers_request_reject, name='volunteers_request_reject'),
    path('volunteers/request/details/<int:pk>/', VolunteersRequestDetailView.as_view(), name='volunteers_request_detail'),
]
