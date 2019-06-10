from django.contrib import admin

from arabic.models import *


class ShaykhAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


class TeacherAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


class StuffAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_fields = ('id',)


class BacthAdmin(admin.ModelAdmin):
	list_display = ('id', 'number')
	readonly_fields = ('id',)


admin.site.register(Shaykh, ShaykhAdmin),
admin.site.register(Teacher, TeacherAdmin),
admin.site.register(Student, StudentAdmin),
admin.site.register(Stuff, StuffAdmin),
admin.site.register(History),
admin.site.register(Bacth, BacthAdmin),