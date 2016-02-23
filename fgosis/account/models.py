from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User,Group
from django.db import models



class Payment(models.Model):
     	GENRE_CHOICES =  (
             ('de', 'Addmision Fees'),
             ('pr', 'Course Fees'),)
	paidstd = models.ForeignKey(User )
	name = models.CharField(max_length=128)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	payment_type = models.CharField(max_length=15,choices=GENRE_CHOICES)
	
	def __str__(self):
		return self.name 

