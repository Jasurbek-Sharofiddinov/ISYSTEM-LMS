from django.db import models

class Lists(models.Model):
	id= models.IntegerField(primary_key=True)
	courseCode= models.CharField(max_length=255)
	name=models.CharField(max_length=255)
	price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
	description=models.TextField(blank=True)
	status=models.BooleanField()
	deleted_at=models.DateTimeField(auto_now=False, auto_now_add=False)

class Modules(models.Model):
	id=models.IntegerField(primary_key=True)
	course_id=models.IntegerField(int)
	name=models.CharField(max_length=255)
	description = models.TextField(blank=True)
	status = models.BooleanField()
	deleted_at=models.DateTimeField(auto_now=False, auto_now_add=False)

class Subjects(models.Model):
	id = models.IntegerField(primary_key=True)
	module_id = models.IntegerField(int)
	course_id = models.IntegerField(int)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	status = models.BooleanField()
	deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False)





