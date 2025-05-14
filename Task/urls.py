from django.urls import path
from .views import TaskListView

app_name = 'task'


urlpatterns = [
    path('task/<int:pk>/', TaskListView.as_view(), name='task_list'),
]
