from django.contrib import admin
from .models import Cv, Comment, Follow, Like

# Register your models here.
admin.site.register(Comment)
admin.site.register(Cv)
admin.site.register(Follow)
admin.site.register(Like)
