from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

message = """
This is a test.
"""

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hubbing.views.home', name='home'),
    # url(r'^hubbing/', include('hubbing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

#    url(r'^$', 'django_twilio.views.say', {'text': message}),
    url(r'^testsms/$', 'callforme.views.testsms'),
    url(r'^sms/$', 'callforme.views.twilio_sms'),
    url(r'^call/$', 'callforme.views.twilio_call')
    # url(r'^$', 'django_twilio.views.conference', {
    #     'name': 'conf1',
    #     'wait_url': 'http://twimlets.com/holdmusic?Bucket=com.twilio.music.rock',
    #     'wait_method': 'GET',
    # }),
)
