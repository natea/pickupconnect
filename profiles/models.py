from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userena.models import UserenaLanguageBaseProfile

import datetime

class Profile(UserenaLanguageBaseProfile):
    """ Default profile """

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile') 

    name =  models.CharField(max_length=255, blank=True)
    phone = models.CharField(_('phone number'), max_length=255, blank=True, null=True)


