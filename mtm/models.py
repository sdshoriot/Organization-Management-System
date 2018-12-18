from django.db import models
from sorl.thumbnail import ImageField


class Authority(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()


class Account(models.Model):
	name = models.CharField(max_length=300, null=True, blank=True)

	def __str__(self):
		return self.name


class Member(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	id_number = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()


class Rule(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	description = models.TextField()


class History(models.Model):
	description = models.TextField()		