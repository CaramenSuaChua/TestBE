from django.urls import path
from .views import StudentAgeStatisticsView

urlpatterns = [
    path('students/age-statistics/', StudentAgeStatisticsView.as_view(), name='student-age-statistics'),
]
