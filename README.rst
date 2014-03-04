========
Feedback
========

Let clients give feedback using Github issues, without them having access to all issues and source code.

Is you are accessing a private repo you will need to set your Github password as an environment variable.
::

    export GITHUB_PASSWORD='your_github_password'

It appears the user needs write access to your repositry in order for them to be able to write issues with labels.

To run in development
::

    python manage.py runserver --settings=feedback.settings.local
