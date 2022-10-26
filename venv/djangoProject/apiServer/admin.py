from django.contrib import admin

from . models import PostExtraDataModel, PostDataModel, BoardModel, BoardExtraColumnModel

admin.site.register(BoardModel) 
admin.site.register(PostDataModel)
admin.site.register(BoardExtraColumnModel)
admin.site.register(PostExtraDataModel)