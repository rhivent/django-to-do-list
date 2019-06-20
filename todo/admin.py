from django.contrib import admin

# Register your models here.
# todo/admin.py
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')

admin.site.register(Todo,TodoAdmin)
