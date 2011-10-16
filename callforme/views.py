# Create your views here.
from django_twilio.decorators import twilio_view
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.dispatch import receiver

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
from twilio.twiml import Response, Sms
from twilio import twiml

from callforme.models import Contact, ContactForm
from userena.signals import activation_complete

account = settings.TWILIO_ACCOUNT_SID
token = settings.TWILIO_AUTH_TOKEN

@twilio_view
def testsms(request):
    r = Response()
    r.append(Sms('Thanks for the SMS message!', to='6175174953'))
    return r
    
def twilio_sms(request):
    """Send a text message using the Twilio API"""
    client = TwilioRestClient(account, token)
    message = client.sms.messages.create(to="+16175174953",
                                         from_="+16175000768",
                                         body="Hello!")
    return render_to_response("hubtext/smssent.html",
                           {"message": message,
                           },
                           RequestContext(request))
    # except:
    #     TwilioRestException('status', 'uri', 'something broke')
        
def twilio_call(request):
    """Make a phone call using the Twilio API"""
    client = TwilioRestClient(account, token)
    
    # call = client.calls.create(to="+16262721760", from_="+14153356842",
    #                            url="http://teddywing.com/twilio_da.xml")
    call = client.calls.create(to="+14153356842", from_="+16175000768",
                               url="http://teddywing.com/twilio_da.xml")
    
    # Steve: 6172901329
    # John: 6262721760
    
    # print call.length
    # print call.sid
    return render_to_response('call.html')
    
def twiml_response(request):
    r = twiml.Response()
    # r.say(text, voice=voice, language=language, loop=loop)
    r.say("Hello we're testing dial assist")
    # with r.dial() as d:
    #   d.number("+14153356842")
    return HttpResponse(r, mimetype='text/xml')

@receiver(activation_complete)
def twilio_verify(sender, **kwargs):
    """ Verify a user's phone with Twilio """
    client = TwilioRestClient(account, token)
    
    user = kwargs['user']
    
    user_profile = user.get_profile()
    print str(user_profile.phone)
    
    validation = client.caller_ids.validate("+" + str(user_profile.phone))
    
    print validation
    # return render_to_response('validation.html',
    #                          {'validation_code' : validation['validation_code']},
    #                          RequestContext(request))

def home(request):
    """depricated"""
    return render_to_response('index.html',
                              context_instance=RequestContext(request))
    #fix this later. this line should never be reached
    if signed_in:
        return render_to_response("index.html")
    else:
        return render_to_response("accounts/signin/")

def contacts(request):
    contact_list = Contact.objects.all().order_by('name')
    return render_to_response('contacts.html', {'contact_list': contact_list},
                              RequestContext(request))

#                              return render_to_response('contacts.html', context_instance = RequestContext(request))

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            new_contact = Contact(user=request.user,
                           name=form.cleaned_data["name"],
                           phone=form.cleaned_data["phone"],
                           birthday=form.cleaned_data["birthday"])
                           
            new_contact.save()

            return HttpResponseRedirect(reverse("contact-detail",
                                                kwargs=dict(contact_id=new_contact.id)))
    else:
        user = request.user
        form = ContactForm(initial={"user": user})
        
        return render_to_response("add_contact.html",
                                  {"form": form,},
                                  RequestContext(request))
                                  
def contact_detail(request):
    return render_to_response('contact_detail.html', {'contact_id': contact_id},
                              RequestContext(request))


