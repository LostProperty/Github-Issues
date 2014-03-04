========
Feedback
========

Let clients give feedback using Github issues, without them having access to all issues and source code.

Getting set-up for development
------------------------------
Is you are accessing a private repo you will need to set your Github password as an environment variable.
::

    export GITHUB_PASSWORD='your_github_password'

It appears the user needs write access to your repositry in order for them to be able to write issues with labels.

Create database and role.
::

    psql -h localhost
    CREATE ROLE feedback LOGIN;
    CREATE DATABASE feedback WITH OWNER feedback ENCODING 'UTF8';

Now sysnc the DB
::

    python manage.py syncdb --migrate

Run the development site
------------------------
::

    export DJANGO_SETTINGS_MODULE=feedback.settings.local
    python manage.py runserver
