
from django.urls import path
from . views import TestView
from .view.tempViews import tempJson

urlpatterns = [
    path('v1/test/', TestView.as_view(), name='test'),
    path('temp', tempJson, name='test2')
]