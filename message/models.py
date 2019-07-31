from django.db import models

# Create your models here.
class Message(models.Model):
	userId = models.IntegerField()
	sender = models.CharField(max_length = 200)
	body = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add=True)
class DoctorMessage(models.Model):
	userId = models.IntegerField()
	sender = models.CharField(max_length = 200)
	body = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add=True)
class Note(models.Model):
	userId = models.IntegerField()
	topic = models.CharField(max_length = 200)
	body = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add=True)
class Notification(models.Model):
	userId = models.IntegerField()
	title = models.CharField(max_length = 200)
	body = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add=True)