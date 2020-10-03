from django.contrib import admin
from .models import ForumPost, Forum, Discussion

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(Forum)
admin.site.register(Discussion)
