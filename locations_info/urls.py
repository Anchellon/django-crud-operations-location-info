from django.urls import path
from locations_info import views

urlpatterns = [
    path('locations/', views.locations_list),
    path('locations/<int:pk>/', views.location_detail),
]