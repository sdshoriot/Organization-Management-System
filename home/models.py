from django.db import models
from sorl.thumbnail import ImageField


class Home(models.Model):
	# Arabic
	arabic_since = models.CharField(max_length=100, null=True, blank=True)
	arabic_name = models.CharField(max_length=100, null=True, blank=True)
	arabic_history = models.TextField()

	# MTM
	mtm_since = models.CharField(max_length=100, null=True, blank=True)
	mtm_name = models.CharField(max_length=200, null=True, blank=True)
	mtm_meaning = models.CharField(max_length=200, null=True, blank=True)
	mtm_history = models.TextField()


class Facility(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()
	

class Message(models.Model):
	img = models.ImageField(upload_to='images', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()


class Feedback(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()