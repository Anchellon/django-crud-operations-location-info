from django.urls import path
from locations_info import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>/', views.LocationDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)