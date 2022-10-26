
import imp
from django.urls import path
from . views import PostDataView
from . views import PostDataDetailView
from . views import BoardView
from . views import BoardDetailView
from . views import BoardExtraColumnDetailView
from . views import BoardExtraColumnView
from . views import PostExtraDataDetailView
from . views import PostExtraDataView

urlpatterns = [
    path('post/', PostDataView.as_view(), name='post'),
    path('post/<int:seq>/', PostDataDetailView.as_view(), name='postDetail'),
    path('board/', BoardView.as_view(), name='board'),
    path('board/<int:seq>/', BoardDetailView.as_view(), name='boardDetail'),
    path('extra/data/', PostExtraDataView.as_view(), name='extraData'),
    path('extra/data/<int:seq>/', PostExtraDataDetailView.as_view(), name='extraDataDetail'),
    path('extra/column/', BoardExtraColumnView.as_view(), name='extraColumn'),
    path('extra/column/<int:seq>/', BoardExtraColumnDetailView.as_view(), name='extraColumnDetail'),
]