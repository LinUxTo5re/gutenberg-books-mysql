from django.urls import path
from .views import GutenbergDataListView

urlpatterns = [
    path('data/', GutenbergDataListView, name='gb-list'),
]
