from django.contrib import admin
from .models import *
# Register your models here.
class Admin(admin.ModelAdmin):
	list_display = ("id", "username", "first_name", "last_name", "number")
	filter_horizontal = ("groups", "user_permissions",)

admin.site.register(CustomUser , Admin)
admin.site.register(Manuscript)