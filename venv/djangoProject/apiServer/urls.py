
from django.urls import path
from . views import BoardCommonDataView

urlpatterns = [
    path('board/', BoardCommonDataView.as_view(), name='board'),
    path('board/<int:seq>/', BoardCommonDataView.as_view(), name='boardDetail'),
]