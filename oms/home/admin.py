from django.contrib import admin

from home.models import *


class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


admin.site.register(Home),
admin.site.register(Facility),
admin.site.register(Message, MessageAdmin),
admin.site.register(Feedback, FeedbackAdmin),