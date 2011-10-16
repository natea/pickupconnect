DialAssist
==========

DialAssist is a web app to automatically call people who are important to you. Just create an account, type in your friends/family and their phone numbers, and DialAssist will call you and them randomly or on a schedule that you specify.

DialAssist was created at the 
`Boston Startup Weekend <http://boston.startupweekend.org>`_ on Oct. 15, 2011.

To install this app (assuming you are on Mac or Linux)::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py

Or if you have easy_install on your machine (don't do this if you did the above)::

    $ sudo easy_install pip
    
Then create the virtualenv::

    $ sudo pip install virtualenv
    $ virtualenv dialassist
    $ cd dialassist
    $ source bin/activate
    (dialassist)$ git clone git@github.com:natea/callme.git
    (dialassist)$ cd callme
    (dialassist)$ pip install -r requirements.txt
    (dialassist)$ python manage.py syncdb
    (dialassist)$ python collectstatic -l
    (dialassist)$ python manage.py runserver
    
Running tests
-------------

To run the tests (later we can integrate nose as the testrunner)::

    $ python manage.py test

Debugging
---------
    
To aid in debugging, set a trace in your code::

    import ipdb; ipdb.set_trace()
    
Resources
=========

Below are the packages that we've used to build DialAssist.

User registration
-----------------

* `django-userena <http://django-userena.org>`_ User profiles, registration, login, password reset, etc.
* `Example django-userena project <https://github.com/bread-and-pepper/django-userena/blob/master/demo_project/>`_
* `django-socialauth  <http://agiliq.com/blog/2009/08/django-socialauth-login-via-twitter-facebook-openi/>`_ Login via Facebook, Twitter, Google, etc.

Twilio
------

`Twilio <http://twilio.com>`_ is a cool service that we use to connect you by phone with your friends and loved ones. 

Thanks to `Rob Spectre <http://brooklynhacker.com>`_ from Twilio for answering all of our questions, providing Twilio credit, and writing this
`thoughtful and inspirational blog post about losing someone you love <http://brooklynhacker.com/post/9243052778/lessons-learned-from-losing-someone-you-love>`_

* `twilio-python <http://readthedocs.org/docs/twilio-python/en/latest/>`_
* `django-twilio <https://github.com/rdegges/django-twilio>`_  
* `django-twilio docs <http://django-twilio.readthedocs.org/en/latest/>`_
* `django-door <https://github.com/sunlightlabs/door-django/>`_ integrating Django with Twilio

Design
------

* `Twitter Bootstrap <http://twitter.github.com/bootstrap>`_ UI framework for building nice-looking web applications
* `famfam icon set <http://www.famfamfam.com/lab/icons/silk/previews/index_abc.png>`_
* `django-famfam <http://link>`_ Cool icons that you can integrate into the design with {% load famfam_icon %} and {% famfam_silk 'building' %} where 'building' is the name of the icon image.

Scheduling
----------

* `django-schedule <https://github.com/thauber/django-schedule>`_ this branch is not maintained so read this `google groups post <https://groups.google.com/d/msg/django-schedule/PnrnW-klH84/soP0jI1C-zEJ>`_ for an update

Mobile
------

* `django-mobile <https://github.com/gregmuellegger/django-mobile>`_ Detects the user agent and lets you serve up different templates depending on the device.

If we wanted to build an API, for example to provide a backend to an iPhone or Android mobile phone app, we could build it with TastyPie.

* `tastypie <https://github.com/toastdriven/django-tastypie>`_
* `tastypie docs <http://django-tastypie.readthedocs.org/en/latest/>`_
