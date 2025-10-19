from django.urls import path
from . import views

app_name = 'hall'

urlpatterns = [
    path('new-hall-creation/', views.new_hall_creation, name='new_hall_creation'),
    path('list/', views.hall_list, name='hall_list'),
    path('facility-creation/', views.facility_creation, name='facility_creation'),
    path('facility-list/', views.facility_list, name='facility_list'),
    path('event-type-creation/', views.event_type_creation, name='event_type_creation'),
    path('event-type-list/', views.event_type_list, name='event_type_list'),
]
