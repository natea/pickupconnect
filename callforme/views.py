# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.dispatch import receiver
from django.core.urlresolvers import reverse

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
from twilio.twiml import Response, Sms
from twilio import twiml

from callforme.models import Contact, ContactForm, User
from userena.signals import activation_complete

account = settings.TWILIO_ACCOUNT_SID
token = settings.TWILIO_AUTH_TOKEN

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
    
    user_profile = request.user.get_profile()
    phone = "+1" + user_profile.phone
    
    call = client.calls.create(to=phone, from_=settings.TWILIO_DEFAULT_CALLERID,
                               url="http://pickupconnect-staging.djangozoom.net/twiml-response/?user_id=%s" %request.user.id)
    
    # Steve: 6172901329
    # John: 6262721760  #6175174953
    
    # print call.length
    # print call.sid
    return render_to_response('call.html', RequestContext(request))
    
def twiml_response(request):
    import random
    
    user = User.objects.filter(id=int(request.GET['user_id']))[0]
    num_contacts = user.contact_set.count()
    contact_select = random.randrange(0, num_contacts) if num_contacts > 1 else 0 # Pick a random contact (fails if you have no contacts)
    
    user_profile = user.get_profile()
    contact = user.contact_set.all()[contact_select]
    
    r = twiml.Response()
    # r.say(text, voice=voice, language=language, loop=loop)
    r.say("Pickup Connect would like to connect you to %s." %contact.name)
    with r.gather(action="http://pickupconnect-staging.djangozoom.net/twiml-connect?contact_id=%s&user_id=%s" %(contact.id, request.GET['user_id']), finishOnKey=1, timeout=15) as g:
        # When we get a background queue, stop using a GET param and take the contact_id from a call
        g.say('Press 1 followed by the pound key to continue connecting.')
        # "... or stay on the line to continue with the call"
    return HttpResponse(r, mimetype='text/xml')

def twiml_connect(request):
    user = User.objects.filter(id=int(request.GET['user_id']))[0]
    
    r = twiml.Response()
    user_profile = user.get_profile()
    
    try:
        contact_phone = ( user.contact_set.filter(id=request.GET['contact_id']) )[0].phone
    except IndexError: # Exception on contact not found
        pass
    
    if 'Digits' in request.POST:
        if request.POST['Digits'] == '1':
            with r.dial(caller_id="+1%s" %user_profile.phone) as d:#caller_id = user->phone
               d.number("+1%s" %contact_phone)
    else:
        r.say('Disconnecting. Thank you for using Pickup Connect.')
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
    contact_list = Contact.objects.filter(user=request.user).order_by('name')
    return render_to_response('contacts.html', {'contact_list': contact_list},
                              RequestContext(request))

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact(user=request.user,
                           name=form.cleaned_data["name"],
                           phone=form.cleaned_data["phone"],
                           birthday=form.cleaned_data["birthday"],
                           twitter=form.cleaned_data["twitter"],
                           frequency=form.cleaned_data["frequency"])
            new_contact.save()
            return HttpResponseRedirect(reverse("contacts"))
            #kwargs=dict(contact_id=new_contact.id
        else:
            # TODO react to invalid form entries
            pass
    else:
        user = request.user
        form = ContactForm(initial={"user": user})
        return render_to_response("add_contact.html",
                                  {"form": form,},
                                  RequestContext(request))
                                  
def contact_detail(request, contact_id):
    contact = Contact.objects.filter(id=contact_id)[0]
    form = ContactForm(initial={"id": contact.id })
    return render_to_response('contact_detail.html', {'contact': contact, 'form': form },
                              RequestContext(request))
