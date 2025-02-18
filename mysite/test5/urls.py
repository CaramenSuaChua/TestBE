from django.urls import path
from .views import TopFurthestPeopleView

urlpatterns = [
    path('people/top-furthest/', TopFurthestPeopleView.as_view(), name='top-furthest'),
]
