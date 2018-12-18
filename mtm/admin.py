from django.contrib import admin

from mtm.models import *


class AuthorityAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_field = ('id',)


class MemberAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'id_number', 'account')
	readonly_field = ('id',)


class RuleAdmin(admin.ModelAdmin):
	list_display = ('id', 'description')
	readonly_field = ('id')


class AccountAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	readonly_field = ('id')


admin.site.register(Authority, AuthorityAdmin),
admin.site.register(Member, MemberAdmin),
admin.site.register(Rule, RuleAdmin),
admin.site.register(History),
admin.site.register(Account, AccountAdmin),