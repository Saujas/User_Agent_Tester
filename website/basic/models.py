# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class BasicUser(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(default='')
	ip = models.GenericIPAddressField(default='')
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.name

