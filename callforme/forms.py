from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.hashcompat import sha_constructor

from userena import settings as userena_settings
from userena.forms import SignupFormOnlyEmail
from userena.models import UserenaSignup

from profiles.models import Profile
 
import random

attrs_dict = {'class': 'required'}

class SignupFormCustomized(SignupFormOnlyEmail):
    """Subclass the SignupFormOnlyEmail for our customized signup form"""
    phone = forms.CharField(
        help_text=Profile._meta.get_field("phone").help_text,
        label=Profile._meta.get_field("phone").verbose_name,
#        initial=Profile._meta.get_field("phone").default,
#        validators=...
        required=True,
    )
    
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                         label=_(u'Terms of Service'),
                         help_text=_(u'I have read and agree to the Terms of Service.'),
                         error_messages={'required': _('You must agree to the terms to register.')})

    # this is taken from userena/forms.py:SignupFormOnlyEmail
    def save(self):
        """ Generate a random username before falling back to parent signup form """
        while True:
            username = sha_constructor(str(random.random())).hexdigest()[:5]
            try:
                User.objects.get(username__iexact=username)
            except User.DoesNotExist: break

        #return super(SignupFormCustomized, self).save()

        username, email, password, phone = (username,
                                     self.cleaned_data['email'],
                                     self.cleaned_data['password1'],
                                     self.cleaned_data['phone'])

        new_user = UserenaSignup.objects.create_user(username,
                                                     email, 
                                                     password,
                                                     not userena_settings.USERENA_ACTIVATION_REQUIRED,
                                                     userena_settings.USERENA_ACTIVATION_REQUIRED)
        new_profile = new_user.get_profile()
        new_profile.phone = phone
        new_profile.save()
        return new_user

