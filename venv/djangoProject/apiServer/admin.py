from django.contrib import admin

from . models import BoardAdditionalDataModel, BoardCommonDataModel, BoardListModel, BoardAdditionalColumnModel

admin.site.register(BoardListModel) 
admin.site.register(BoardCommonDataModel)
admin.site.register(BoardAdditionalColumnModel)
admin.site.register(BoardAdditionalDataModel)