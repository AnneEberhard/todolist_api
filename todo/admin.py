from django.contrib import admin
from .models import Todo, Message

class TodoAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'user')


admin.site.register(Todo,TodoAdmin)
admin.site.register(Message)
