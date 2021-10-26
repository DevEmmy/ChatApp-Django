from django.contrib import admin
from .models import Group, Message
# Register your models here.

class GroupAdmin(admin.ModelAdmin):
	list_display = ('group_name', 'slug',)
	prepopulated_fields = {'slug':('group_name',)}

admin.site.register(Group, GroupAdmin)
admin.site.register(Message)

