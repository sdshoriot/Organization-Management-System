from django.db import models

from mtm.models import Authority, Member


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


class Message(models.Model):
	authority = models.ForeignKey(Authority, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	designation = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()


class Feedback(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()