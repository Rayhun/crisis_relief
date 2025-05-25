# core/urls.py
from django.urls import path
from .views import dashboard, auth, user

app_name = 'core'

urlpatterns = [
    path('', dashboard.DashboardView.as_view(), name='dashboard'),
    path('albania-map/', dashboard.AlbaniaMapView.as_view(),
         name='albania_map'),
    path('login/', auth.CustomLoginView.as_view(), name='login'),
    path('signup/', auth.SignupView.as_view(), name='signup'),
    path('logout/', auth.logout_view, name='logout'),
    path('user/list/', user.UserListView.as_view(), name='user_list'),
    path('profile/<int:pk>/', user.UserProfileView.as_view(),
         name='user_profile'),
    path('update-profile/', user.update_profile, name='update_profile'),
    path('affected-people-images/',
         dashboard.AffectedPeopleImagesView.as_view(),
         name='affected_people_images'),
]
