from django.urls import path
from .views import TopAgeDifferenceView

urlpatterns = [
    path('people/top-age-difference/', TopAgeDifferenceView.as_view(), name='top-age-difference'),
]
