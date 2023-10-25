from django.contrib import admin
from .models import Room, Message
# Register your models here.

admin.site.register(Message)
admin.site.register(Room)