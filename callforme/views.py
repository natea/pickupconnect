# Create your views here.
from twilio.twiml import Response, Sms
from django_twilio.decorators import twilio_view
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
from django.conf import settings

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

    call = client.calls.create(to="+16175174953", from_="+15083040360",
                               url="http://foo.com/call.xml", status_code="")
    return call
    # print call.length
    # print call.sid

def home(request):
    return render_to_response("index.html")
