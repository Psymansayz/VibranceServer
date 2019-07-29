from django.db import models
from jsonfield import JSONField

# Create your models here.
class Medication(models.Model):
	userId = models.IntegerField()
	name = models.CharField(max_length = 200)
	color = models.CharField(max_length = 100)
	dosage = models.CharField(max_length = 300)
	frequency = models.CharField(max_length = 200)
	refillDate = models.CharField(max_length = 100)
	adherence = JSONField()