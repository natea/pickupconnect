from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    birthday = models.DateField(blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    
    FREQUENCY_CHOICES = (
        ('W', 'Weekly'),
        ('B', 'Bi-weekly'),
        ('M', 'Monthly'),
        )
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('user',)
        
class Call(models.Model):
    user = models.ForeignKey(User)
    contact = models.ForeignKey(Contact)
    time = models.DateTimeField(auto_now_add = True)
   