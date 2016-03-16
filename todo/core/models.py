from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class project(models.Model):
	name = models.CharField(max_length=100,unique=True)
	description = models.TextField()
	startdate = models.DateTimeField()
	enddate = models.DateTimeField()
	created_at = models.DateField(default=timezone.now)
	#updated_at = models.DatetimeField(auto_now_add=True)

	def __unicode__(self):
            return self.name

	
class maintask(models.Model):
	project = models.ForeignKey(project)
	name = models.CharField(max_length=100,unique=True)
        description = models.TextField()
        startdate = models.DateTimeField()
        enddate = models.DateTimeField()
        created_at = models.DateField(default=timezone.now)
        #updated_at = models.AutoDateTimeField(default=timezone)

	def __unicode__(self):
            return self.name

class subtask(models.Model):
	maintask = models.ForeignKey(maintask)
        name = models.CharField(max_length=100,unique=True)
        description = models.TextField()
        startdate = models.DateTimeField()
        enddate = models.DateTimeField()
        created_at = models.DateField(default=timezone.now)
       # updated_at = models.AutoDateTimeField(default=timezone)

	def __unicode__(self):
            return self.name

class todo(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField()
	created = models.DateTimeField()

	def __unicode__(self):
	    return self.name


