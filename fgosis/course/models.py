from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User,Group
from django.db import models

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=10,unique=True)
	name = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	theory_hrs= models.IntegerField(default=0)
	practical_hrs = models.IntegerField(default=0)
	course_creator = models.ForeignKey(User)
  	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
	
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
			self.slug = slugify(self.name)
			super(Course, self).save(*args, **kwargs)
	def __str__(self):
		return  self.name

class CourseModule(models.Model):
	course = models.ForeignKey(Course)
	code = models.CharField(max_length=10,unique=True)
	name = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	theory_hrs= models.IntegerField(default=0)
	practical_hrs = models.IntegerField(default=0)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
			self.slug = slugify(self.name)
			super(CourseModule, self).save(*args, **kwargs)
	

	
	def __str__(self):
		return self.name

class Topic(models.Model):
	course_module = models.ForeignKey(CourseModule)
	code = models.CharField(max_length=15,unique=True)
	name = models.CharField(max_length=128)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	theory_hrs= models.IntegerField(default=0)
	practical_hrs = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name 
		


class Lesson(models.Model):
	topic = models.ForeignKey(Topic)
	code = models.CharField(max_length=5,unique=True)
	name = models.CharField(max_length=128)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	duration = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name 
		
class Activity(models.Model):
	GENRE_CHOICES1 =  (
             ('de', 'Demostration'),
             ('pr', 'Presentation'),
             ('ex', 'Exercise'),
             ('as', 'Assignment'),
             ('pr', 'Project'),
             ('db', 'Debate'), 
             ('qu', 'Questining'),    
             )
	GENRE_CHOICES2 = ( ('t', 'Theory'),('p','Practical'),('l','Lab'),)
	leson = models.ForeignKey(Lesson)
	code = models.CharField(max_length=5,unique=True)
	name = models.CharField(max_length=128)
	fees = models.DecimalField(max_digits=16, decimal_places=2,default=0.00)
	duration = models.IntegerField(default=0)
	activity_type = models.CharField(max_length=15,choices=GENRE_CHOICES1)
	session = models.CharField(max_length=15,choices=GENRE_CHOICES2)
	iscompleted = models.BooleanField()
	
	def __str__(self):
		return self.name 


class CourseGroup(models.Model):

	course = models.ForeignKey(Course)
	code = models.CharField(max_length=15, unique=True)
	name = models.CharField(max_length=128)
	student = models.ManyToManyField(User, related_name="student")
  	teacher = models.ForeignKey(User)
  	
  	def __str__(self):
		return self.name 

class Teachers_Diary(models.Model):
	activity = models.ForeignKey(Activity)
	coursegroup = models.ForeignKey(CourseGroup)
        completed = models.BooleanField()
	tobecompleted = models.DateTimeField(auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)

	

class Theory_Lesson_Schedule(models.Model):
	activity = models.ForeignKey(Activity)
	tobecompleted = models.DateTimeField(auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
	coursegroup = models.ForeignKey(CourseGroup)
	
	def __str__(self):
		return self.activity

class Practical_Lesson_Schedule(models.Model):
	activity = models.ForeignKey(Activity)
	tobecompleted = models.DateTimeField(auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
	coursegroup = models.ForeignKey(CourseGroup)
	
	def __str__(self):
		return self.activity
	

