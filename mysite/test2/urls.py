from django.urls import path
from .views import RetrieveHtmlFile

urlpatterns = [
    path('get_html_file/', RetrieveHtmlFile.as_view(), name='get_html_file'),
]
