=====
KBIMS Reptile
=====

This is a reptile module for kbims

Note that FISH is under development and not yet feature complete.

The latest source code is available at http://github.com/kartoza/kbims-reptile.

* **Developers:** See our `developer guide`_


Project Activity
--------------

|ready| |inprogress|

|throughput_graph|

* Current test status master: |test_status_master| 

* Current test status develop: |test_status_develop| 


Quick Installation Guide
------------------------
For deployment we use `docker`_ so you need to have docker
running on the host. HealthyRivers is a django app so it will help if you have
some knowledge of running a django site.

    git clone git://github.com/kartoza/kbims-reptile.git
    
    make build
    
    make permissions
    
    make web
    
    # Wait a few seconds for the DB to start before to do the next command
    
    make migrate
    
    make collectstatic
    

So as to create your admin account:
```
make superuser
```


Install as a Django Package
---------------------------

1. Add "reptile" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        'reptile',
    ]

2. Include the reptile URLconf in your project urls.py like this:

    path('reptile/', include('reptile.urls'))

3. Run `python manage.py migrate` to create the reptile models.


Thank you
_________

Thank you to the individual contributors who have helped to build HealthyRivers:

* Christian Christelis (Lead developer): christian@kartoza.com
* Tim Sutton (Lead developer): tim@kartoza.com
* Dimas Ciptura: dimas@kartoza.com
* Irwan Fathurrahman: irwan@kartoza.com
* Alison Mukoma: alison@kartoza.com
* Anita Hapsari: anita@kartoza.com

.. _developer guide: https://github.com/kartoza/healthyrivers/blob/develop/README-dev.md
.. _docker: http://docker.com
.. |ready| image:: https://badge.waffle.io/kartoza/kbims-reptile.svg?label=ready&title=Ready
.. |inprogress| image:: https://badge.waffle.io/kartoza/kbims-reptile.svg?label=in%20progress&title=In%20Progress
.. |throughput_graph| image:: https://graphs.waffle.io/kartoza/kbims-reptile/throughput.svg
.. |test_status_master| image:: https://travis-ci.org/kartoza/kbims-reptile
.svg?branch=master
.. |test_status_develop| image:: https://travis-ci.org/kartoza/kbims-reptile.svg?branch=develop
.. |nbsp| unicode:: 0xA0
   :trim:
