from django.db import models


class Notice(models.Model):
	heading = models.CharField(max_length=200, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	description = models.TextField()