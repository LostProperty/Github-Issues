========
Feedback
========

Let clients give feedback using Github issues, without them having access to all issues and source code.

Getting set-up for development
------------------------------
Is you are accessing a private repo you will need to set your Github password as an environment variable.
::

    export GITHUB_PASSWORD='your_github_password'
    export GITHUB_USER='your_github_username'

It appears the user needs write access to your repositry in order for them to be able to write issues with labels.

Create database and role.
::

    psql -h localhost
    CREATE ROLE feedback LOGIN CREATEDB;
    CREATE DATABASE feedback WITH OWNER feedback ENCODING 'UTF8';

or::

    createuser feedback --createdb --login
    createdb --owner feedback --encoding='utf-8' --template=template0 feedback

.. note::

    1. The database instructions provided here are postgres specific
    2. We create the feedback role without a password. The application
       settings default to using password-less connections. You may need to
       create a different settings module or adjust pg_hba.conf to allow
       connection without passwords

Now sync the DB
::

    python manage.py syncdb --migrate

Run the development site
------------------------
::

    export DJANGO_SETTINGS_MODULE=feedback.settings.local
    python manage.py runserver

To run the tests
----------------
::

    py.test

Note you may need to run ``add2virtualenv .`` do py.test can find the your setting corrrectly.
