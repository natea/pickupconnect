# Create your views here.
from twilio.twiml import Response, Sms
from twilio import twiml
from django_twilio.decorators import twilio_view
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.http import HttpResponse

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
    
    call = client.calls.create(to="+15083040360", from_="+14153356842",
                               url="http://p00000563.djangozoom.net/twiml-response/")
    # print call.length
    # print call.sid
    return render_to_response('call.html')
    
def twiml_response(request):
    r = twiml.Response()
    # r.say(text, voice=voice, language=language, loop=loop)
    r.say("Calling you")
    with r.dial() as d:
      d.number("+14153356842")
    return HttpResponse(r, mimetype='text/xml')

def twilio_verify(request):
    """ Verify a user's phone with Twilio """
    client = TwilioRestClient(account, token)
    
    #validation = client.callerids.validate("""PHONE NUMBER""")
    
    validation = {'validation_code' : "613332"}
    
    return render_to_response('validation.html',
                             {'validation_code' : validation['validation_code']},
                             RequestContext(request))

def home(request):
    return render_to_response("index.html")
