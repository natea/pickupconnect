from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupFormOnlyEmail

from profiles.models import Profile

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

        self.cleaned_data['username'] = username
        
        # TODO: need code to save phone number to profile record
        
        return super(SignupFormCustomized, self).save()