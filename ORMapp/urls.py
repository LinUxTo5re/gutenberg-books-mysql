from django.urls import path
from .views import *

urlpatterns = [
    path('data/', GutenbergDataListView, name='gb-list'),
    ]
