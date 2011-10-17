PickupConnect
=============

PickupConnect is a web app to automatically call people who are important to you. Just create an account, type in your friends/family and their phone numbers, and pickupconnect will call you and them randomly or on a schedule that you specify.

PickupConnect was created at the `Boston Startup Weekend <http://boston.startupweekend.org>`_ Oct. 15-16, 2011.

To install this app (assuming you are on Mac or Linux)::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py

Or if you have easy_install on your machine (don't do this if you did the above)::

    $ sudo easy_install pip
    
Then create the virtualenv::

    $ sudo pip install virtualenv
    $ virtualenv pickupconnect --no-site-packages
    $ cd pickupconnect
    $ source bin/activate
    (pickupconnect)$ git clone git@github.com:natea/callme.git
    (pickupconnect)$ cd pickupconnect
    (pickupconnect)$ pip install -r requirements.txt
    (pickupconnect)$ python manage.py syncdb
    (pickupconnect)$ python collectstatic -l
    (pickupconnect)$ python manage.py runserver
    
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

Below are some of the packages that we've used to build PickupConnect, or are considering using as the app matures.

Users
-----

* `django-userena <http://django-userena.org>`_ User profiles, registration, login, password reset, etc.
* `Example django-userena project <https://github.com/bread-and-pepper/django-userena/blob/master/demo_project/>`_
* `django-socialauth  <http://agiliq.com/blog/2009/08/django-socialauth-login-via-twitter-facebook-openi/>`_ Login via Facebook, Twitter, Google, etc.
* `django-badger <https://github.com/lmorchard/django-badger>`_ award badges to most active users
* `django-activity-stream <https://github.com/justquick/django-activity-stream>`_ display a stream of user's activity

Contacts
--------

* `django-contacts-import <https://github.com/eldarion/django-contacts-import/>`_ import your Yahoo, Google or vCard contacts.
* `csvkit <https://github.com/onyxfish/csvkit>`_ bunch of tools to work with CSV files. Useful for importing people's contact lists

Twilio
------

`Twilio <http://twilio.com>`_ is a cool service that we use to connect you by phone with your friends and loved ones. 

Thanks to `Rob Spectre <http://brooklynhacker.com>`_ from Twilio for answering all of our questions, providing Twilio credit, and writing this
`thoughtful and inspirational blog post about losing someone you love <http://brooklynhacker.com/post/9243052778/lessons-learned-from-losing-someone-you-love>`_

* `twilio-python <http://readthedocs.org/docs/twilio-python/en/latest/>`_
* `django-twilio <https://github.com/rdegges/django-twilio>`_  
* `django-twilio docs <http://django-twilio.readthedocs.org/en/latest/>`_
* `django-door <https://github.com/sunlightlabs/door-django/>`_ integrating Django with Twilio
* `django-twilio-utils <https://github.com/bnmrrs/django-twilio-utils>`_

Form Fields
-----------

* `USPhoneNumberWidget <http://hustoknow.blogspot.com/2010/10/usphonenumberwidget.html>`_ 

Design
------

* `Twitter Bootstrap <http://twitter.github.com/bootstrap>`_ UI framework for building nice-looking web applications
* `compress-twitter-bootstrap <https://github.com/vwall/compass-twitter-bootstrap>`_ Twitter Bootstrap ported to Compass (Ruby)
* `famfam icon set <http://www.famfamfam.com/lab/icons/silk/previews/index_abc.png>`_
* `django-famfam <http://link>`_ Cool icons that you can integrate into the design with {% load famfam_icon %} and {% famfam_silk 'building' %} where 'building' is the name of the icon image.

HTML5 Boilerplate
-----------------

We're not using this right now, but if we wanted to make the site work better on mobile devices, it might be worth switching to this.

* `html5boilerplate <http://html5boilerplate.com/>`_ HTML5 Boilerplate is the professional badass's base HTML/CSS/JS template for a fast, robust and future-proof site.
* `django-html5-boilerplate <https://github.com/mike360/django-html5-boilerplate>`_ A Django project starting template with html5-boilerplate integrated.
* `django-cms-html5-1140px-boilerplate <https://github.com/bitmazk/django-cms-html5-1140px-boilerplate>`_ A django-cms project starting template with html5-boilerplate integrated

Scheduling
----------

We're not using these yet, but if we wanted to build better scheduling of the best times to call, we could use these packages.

* `django-schedule <https://github.com/thauber/django-schedule>`_ this branch is not maintained so read this `google groups post <https://groups.google.com/d/msg/django-schedule/PnrnW-klH84/soP0jI1C-zEJ>`_ for an update
* `glamkit-eventtools <http://docs.glamkit.org/documentation/eventtools/index.html>`_ a fork of django-schedule that is like more up-to-date.

Mobile
------

* `django-mobile <https://github.com/gregmuellegger/django-mobile>`_ Detects the user agent and lets you serve up different templates depending on the device.

If we wanted to build an API, for example to provide a backend to an iPhone or Android mobile phone app, we could build it with TastyPie.

* `tastypie <https://github.com/toastdriven/django-tastypie>`_
* `tastypie docs <http://django-tastypie.readthedocs.org/en/latest/>`_

Performance
-----------

* `django-media-brute <https://github.com/Brant/django-mediabrute>`_ Automatic collecting, compiling, and minifying of CSS and JS for Django projects