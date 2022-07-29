from django.contrib import admin
from .models import FreePost, Comment, Check

admin.site.register(FreePost)
admin.site.register(Comment)
admin.site.register(Check)