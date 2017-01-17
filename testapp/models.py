from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestContent(models.Model):
	content_text = models.TextField()