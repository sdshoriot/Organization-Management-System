from django.db import models
from sorl.thumbnail import ImageField
	

class Shaykh(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	biography = models.TextField()


class Teacher(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	biography = models.TextField()


class Bacth(models.Model):
	number = models.CharField(max_length=20)

	def __str__(self):
		return self.number


class Student(models.Model):
	bacth = models.ForeignKey(Bacth, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	biography = models.TextField()


class Stuff(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)


class History(models.Model):
	description = models.TextField()	