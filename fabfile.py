#!/usr/bin/env python
from fabric.api import local

def deploy():
    """
    Deploy the latest version to Heroku
    """
    # Push changes to master
    local("git push github master")

    # Push changes to Heroku
    local("git push heroku master")

    # Run migrations on Heroku
    local("heroku run python manage.py migrate")