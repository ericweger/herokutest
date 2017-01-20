from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestContent(models.Model):
	content_text = models.TextField()
	content_name = models.CharField(max_length=50, blank=True)
	def save(self, *args, **kwargs):
		if not self.content_name:
			self.content_name = "Section"+self.id
		super(TestContent, self).save(*args, **kwargs)