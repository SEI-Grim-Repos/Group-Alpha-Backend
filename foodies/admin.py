from django.contrib import admin
from .models import User_Account, Post, Comment

# Register your models here.

admin.site.register(User_Account)
admin.site.register(Post)
admin.site.register(Comment)