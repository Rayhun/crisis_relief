from django.urls import path
from Affected.views import event, relief, ajax


app_name = 'affected'


urlpatterns = [
    path('events/', event.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', event.EventDetailView.as_view(),
         name='event_detail'),
    path('events/create/', event.EventCreateView.as_view(),
         name='event_create'),
    path('events/update/<int:pk>/', event.EventUpdateView.as_view(),
         name='event_edit'),
    path('events/delete/<int:pk>/', event.EventDeleteView.as_view(),
         name='event_delete'),
    # Relief Request URLs =====================================================
    path('relief-request', relief.ReliefRequestListView.as_view(),
         name='relief_request_list'),
    path('relief-request/<int:pk>/', relief.ReliefRequestDetailView.as_view(),
         name='relief_request_detail'),
    path('relief-request/create/', relief.ReliefRequestCreateView.as_view(),
         name='relief_request_create'),
    path('relief-request/update/<int:pk>/',
         relief.ReliefRequestUpdateView.as_view(),
         name='relief_request_edit'),
    path('relief-request/delete/<int:pk>/',
         relief.ReliefRequestDeleteView.as_view(),
         name='relief_request_delete'),

    # AJAX URL for deleting an event
    path('events/delete/<int:event_id>/', ajax.get_event_delete,
         name='ajax_event_delete'),
    path('relief/request/delete/<int:relief_request_id>/',
         ajax.get_relief_request_delete, name='ajax_relief_request_delete'),
]
