from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestContent(models.Model):
	id = models.AutoField(primary_key=True)
	content_text = models.TextField()
	content_name = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return self.content_name
	def save(self, *args, **kwargs):
		if not self.content_name:
			self.content_name = "Section "+str(self.id)
		super(TestContent, self).save(*args, **kwargs)