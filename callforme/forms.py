from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm

from profiles.models import Profile

attrs_dict = {'class': 'required'}

class SignupFormCustomized(SignupForm):

    phone = forms.CharField(
        help_text=Profile._meta.get_field("phone").help_text,
        label=Profile._meta.get_field("phone").verbose_name,
        initial=Profile._meta.get_field("phone").default,
#        validators=...
        required=True,
    )
    
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                         label=_(u'Terms of Service'),
                         help_text=_(u'I have read and agree to the Terms of Service.'),
                         error_messages={'required': _('You must agree to the terms to register.')})