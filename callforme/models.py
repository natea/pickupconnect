from django.db import models
from django.contrib.auth.models import User
 

class Contact(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	birthday = models.DateField()

	FREQUENCY_CHOICES = (
		('W', 'Weekly'),
	        ('B', 'Bi-weekly'),
		('M', 'Monthly'),
    	)
	frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES)

class Call(models.Model):
	user = models.ForeignKey(User)
	contact = models.ForeignKey(Contact)
	time = models.DateTimeField(auto_now_add = True)
   
