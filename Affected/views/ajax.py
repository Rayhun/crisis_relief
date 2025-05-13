# ajax
from django.http import JsonResponse
from Affected.models import Event, ReliefRequest


def get_event_delete(request, event_id):
    """
    Handle the deletion of an event.
    """
    if request.method == 'POST':
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'status': 'success'})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def get_relief_request_delete(request, relief_request_id):
    """
    Handle the deletion of a relief request.
    """
    if request.method == 'POST':
        try:
            relief_request = ReliefRequest.objects.get(id=relief_request_id)
            relief_request.delete()
            return JsonResponse({'status': 'success'})
        except ReliefRequest.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Relief request not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
