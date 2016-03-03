from __future__ import unicode_literals

from django.db import models

# Create your models here.


class YouTube(models.Model):
	title = models.CharField(max_length=200, null=False, blank=False)
	description = models.TextField(default='not found any descriptions')
	class Meta:
		ordering = ('title',)

	def __unicode__(self):
		return unicode(self.id)