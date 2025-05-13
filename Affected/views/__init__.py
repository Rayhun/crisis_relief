from .event import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)
from .relief import (
    ReliefRequestListView,
    ReliefRequestDetailView,
    ReliefRequestCreateView,
    ReliefRequestUpdateView,
    ReliefRequestDeleteView,
)
from .ajax import get_event_delete, get_relief_request_delete


__all__ = [
    "EventListView",
    "EventDetailView",
    "EventCreateView",
    "EventUpdateView",
    "EventDeleteView",
    "get_event_delete",
    "ReliefRequestListView",
    "ReliefRequestDetailView",
    "ReliefRequestCreateView",
    "ReliefRequestUpdateView",
    "ReliefRequestDeleteView",
    "get_relief_request_delete",
]
