.. _Git: https://git-scm.com/
.. _pip: https://pip.pypa.io/en/stable/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
.. _Docker: https://www.docker.com/
.. _Docker Compose: https://github.com/docker/compose
.. _autodock-paas: https://github.com/prologic/autodock-paas
.. _circuits: http://circuitsframework.com/
.. _circuits.web: http://circuitsweb.com/
.. _PureCSS: http://purecss.io/
.. _Contact Me: http://prologic.shortcircuit.net.au/

circuits + circuits.web + PureCSS Starter Kit
=============================================

This a starter kit combining the following technologies:

- `circuits`_ and it's `circuits.web`_ frameworks. -- Powerful components for your applications.
- `PureCSS`_ -- A set of small, responsive CSS modules that you can use in every web project.


Quick Start
-----------

With `git`_, `virtualenvwrapper`_ and `pip`_:

.. code-block:: bash
    
    git clone https://github.com/prologic/circuits_purecss_starter.git
    cd circuits_purecss_starter
    mkvirtualenv circuits_purecss_start
    pip install -r requirements.txt
    ./server.py

Visit: http://localhost:8000//

With `Docker`_ and `Docker Compose`_:

.. code-block:: bash
    
    git clone https://github.com/prologic/circuits_purecss_starter.git
    cd circuits_purecss_starter
    docker-compose build
    docker-compose up

.. note:: You need (*and should use*) `autodock-paas`_ for this.

----

A live demo can be viewed here: http://circuits_purecss_starter.vz1.bne.shortcircuit.net.au/
(If the demo is down please `Contact Me`_).

Enjoy :)
