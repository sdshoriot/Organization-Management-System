from django.contrib import admin

from notice.models import Notice


class NoticeAdmin(admin.ModelAdmin):
	list_display = ('id', 'heading')
	readonly_fields = ('id',)


admin.site.register(Notice, NoticeAdmin),