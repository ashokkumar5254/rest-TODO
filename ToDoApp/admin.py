from django.contrib import admin

# Register your models here.
from .models import todo_model
admin.site.register(todo_model)
