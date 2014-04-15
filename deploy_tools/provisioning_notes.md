Provisioning a new site
=================================

##Required packages:

*nginx      - sudo apt-get install nginx
*python3.4  - Follow installion instructions from google drive
*git-core   - sudo apt-get install git-core
*pyvenv    - comes with python34 create "env1" virtual environment
**gunicorn   - pip install it within virtual environment "env1"
**Django 1.7b - pip install  it within virtual environment "env1"

## Nginx Virtual Host config:

*see nginx.template.conf under deploy_tools
*replace SITENAME with name of the site

##Upstart job:

*see gunicorn-upstart.template.conf under deploy tools
*replace SITENAME with name of the site


## Site structure

Assuming we have a /home/username:

/home/username
|__sites
    |__SITENAME
       |__database
       |__source
       |__static
       |__virtualenv   (not needed with pyvenv)
