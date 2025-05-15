from django.urls import path
from .views import TaskListView, task_self_assign

app_name = 'task'


urlpatterns = [
    path('task/<int:pk>/', TaskListView.as_view(), name='task_list'),
    path('task/self-assign/<int:pk>/', task_self_assign, name='task_self_assign'),
]
