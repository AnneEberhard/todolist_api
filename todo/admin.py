from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'user')


admin.site.register(Todo,TodoAdmin)
