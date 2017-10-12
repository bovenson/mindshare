from django.contrib import admin
from mindmap.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(MindMap)
admin.site.register(MindMapVote)
admin.site.register(FeedbackMessage)
admin.site.register(Article)
