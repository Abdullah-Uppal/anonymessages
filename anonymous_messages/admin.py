from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
# Register your models here.

user = get_user_model()

admin.site.unregister(user)

class UrlInline(admin.TabularInline):
  extra = 0
  model = URL
  fields = ['name', 'time_created', ]

class UserAdmin(admin.ModelAdmin):
  model = user
  inlines = [UrlInline]

admin.site.register(user, UserAdmin)

class MessageInline(admin.TabularInline):
  extra = 0
  model = AnonymousMessage
  fields = ['message', 'time_created', ]

class URLAdmin(admin.ModelAdmin):
  model = URL
  inlines = [MessageInline]

admin.site.register(URL, URLAdmin)
admin.site.register(AnonymousMessage)