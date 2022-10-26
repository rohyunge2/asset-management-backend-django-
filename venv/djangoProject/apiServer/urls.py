
import imp
from django.urls import path
from . views import BoardCommonDataView
from . views import BoardCommonDataDetailView
from . views import BoardListView

urlpatterns = [
    path('post/', BoardCommonDataView.as_view(), name='post'),
    path('post/<int:seq>/', BoardCommonDataDetailView.as_view(), name='postDetail'),
    path('board/', BoardListView.as_view(), name='board'),
]