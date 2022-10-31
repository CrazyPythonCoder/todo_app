from django.contrib import admin
from .models import TodoUser, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(TodoUser)