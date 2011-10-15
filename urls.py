from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.conf import settings
#from urls.urlpatterns import RegexURLPattern

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

message = """
This is a test.
"""

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'callforme.views.home', name='home'),
    # url(r'^hubbing/', include('hubbing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

#    url(r'^$', 'django_twilio.views.say', {'text': message}),
    url(r'^testsms/$', 'callforme.views.testsms'),
    url(r'^sms/$', 'callforme.views.twilio_sms'),
    url(r'^call/$', 'callforme.views.twilio_call'),
    url(r'^verify\-phone/$', 'callforme.views.twilio_verify')
    
    # account stuff using userena
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^$',
        direct_to_template,
        {'template': 'static/promo.html'},
        name='promo'),
    url(r'^i18n/', include('django.conf.urls.i18n')),    
    # url(r'^$', 'django_twilio.views.conference', {
    #     'name': 'conf1',
    #     'wait_url': 'http://twimlets.com/holdmusic?Bucket=com.twilio.music.rock',
    #     'wait_method': 'GET',
    # }),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
)
